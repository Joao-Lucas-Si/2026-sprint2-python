#include <Arduino.h>

// Biblioteca para usar o KeyPad que identifi a tecla
#include <Keypad.h>

#include <HTTPClient.h>

// Biblioteca para utilizar o Wifi
#include <WiFi.h>
// Biblioteca util para utilizar a biblioteca de abaixo
#include <Wire.h>
// Biblioteca para usar o Display
#include <LiquidCrystal_I2C.h>

// Configurando o Display
LiquidCrystal_I2C LCD = LiquidCrystal_I2C(0x27, 16, 2);

/// Informação do KayPad
// Declarando o tamanho do KeyPad
const byte LINHAS = 4;
const byte COLUNAS = 4;

// conteudo dos botões
char teclas[LINHAS][COLUNAS] = {
    {'1', '2', '3', 'A'},
    {'4', '5', '6', 'B'},
    {'7', '8', '9', 'C'},
    {'*', '0', '#', 'D'}};

// Informando onde esta conectado cada um
byte pinosLinhas[LINHAS] = {13, 14, 27, 26};
byte pinosColunas[COLUNAS] = {25, 33, 32, 23};

// Juntando tudo
Keypad teclado = Keypad(
    makeKeymap(teclas),
    pinosLinhas,
    pinosColunas,
    LINHAS,
    COLUNAS);

// Função que vai ser executada até que o ESP32 se conecte
void spinner()
{
  static int8_t counter = 0;
  const char *glyphs = "\xa1\xa5\xdb";
  LCD.setCursor(15, 1);
  LCD.print(glyphs[counter++]);
  if (counter == strlen(glyphs))
  {
    counter = 0;
  }
}

// Booleano que define se o keypad funciona ou não
bool acessoPermitido = false;

// Variavel que vai guardar o que for escrito
String codigo = "";

String requisitar(String endpoint)
{
  HTTPClient http;
  http.useHTTP10(true);
  http.begin("http://host.wokwi.internal:5000/" + endpoint);
  http.GET();
  String result = http.getString();
  return result;
}

// Função de carregamento
void carregador()
{
  // A bateria atual do carro que vai até o 100%
  int bateria = 0;
  int poder = 2;
  String result = requisitar("ocpp/startTransaction/" + codigo);
  int quantidade = result.toInt();
  while (bateria <= quantidade)
  {

    LCD.setCursor(5, 0);
    LCD.println("CARREGANDO");

    LCD.setCursor(9, 1);
    LCD.print(bateria);
    // LCD.print("%");

    requisitar("/ocpp/MeterValue/" + codigo + "/" + poder);
    bateria += poder;
    delay(500);
    LCD.clear();
  }
  LCD.setCursor(6, 3);
  LCD.print("Recarga");
  LCD.setCursor(5, 2);
  LCD.print("Terminada");

  // delay(200);
  LCD.clear();
  acessoPermitido = false;
  return;
}

// Função que vai verificar o codigo
void ValidCode()
{
  try
  {
    String result = requisitar("ocpp/verificar-codigo/" + codigo);

    // Se o codigo digitado for igual ao codigo permitido ,vai entrar
    if (result == "1")
    {
      // Mudando o acesso para true e bloqueando o keypad
      acessoPermitido = true;
      LCD.clear();

      LCD.setCursor(0, 3);
      LCD.print("Entrada");
      LCD.setCursor(0, 2);
      LCD.print("Permitida");

      delay(2000);
      LCD.clear();
      // Chamando a função carregador
      carregador();
      codigo = "";
    }
    // Se não , então vai ter que tentar novamente
    else
    {
      LCD.clear();
      LCD.setCursor(0, 3);
      LCD.print("Codigo");
      LCD.setCursor(0, 2);
      LCD.print("Invalido");

      codigo = "";
      delay(2000);
      LCD.clear();
    }
  }
  catch (const char *msg)
  {
    Serial.print(msg);
  }
}

// Função onde mostramos as informções no Display
void setup()
{
  Serial.begin(115200);

  // inicia o Display
  LCD.init();
  LCD.backlight();

  // Utiliza a primeira linha do Display
  LCD.setCursor(0, 0);
  LCD.print("Connecting to ");

  // Utiliza a segunda linha
  LCD.setCursor(0, 1);
  LCD.print("WiFi ");

  // Faz a conexão com o Wifi
  WiFi.begin("Wokwi-GUEST", "", 6);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(250);
    // chama a função que tenta novamente a conexão se tiver algum problema
    spinner();
  }

  // localhost/carregar
  //
  //
  //

  // Limpa o Display
  LCD.clear();

  LCD.setCursor(0, 0);
  LCD.println("WiFi");
  LCD.setCursor(0, 1);
  LCD.println("Connected");
  // Tempo de espera de 1 segundos
  delay(1000);
  LCD.clear();
}

void loop()
{

  if (!acessoPermitido)
  {
    // Pegando as informação das teclas
    char tecla = teclado.getKey();

    if (tecla)
    {
      // Se a tecla for * vai remover o ultimo caracter
      if (tecla == '*')
      {
        // Para remover o ultimo caracter tem que ter pelo menos um caracter
        if (codigo.length() > 0)
        {
          // Removendo o ultimo caracter
          codigo.remove(codigo.length() - 1);
        }
      }
      // Se a tecla for # quer dizer 'enviar'
      else if (tecla == '#')
      {
        // Verificador de validade
        ValidCode();
        delay(100);
        return;
      }
      else
      {
        // Se a pessoa não digitar #, pode continuar escrevendo
        if (codigo.length() < 6)
        {
          codigo += tecla;
        }
      }
      LCD.clear();
      LCD.setCursor(0, 0);
      LCD.println("Digite o codigo:");
      LCD.setCursor(0, 3);
      LCD.println(codigo);
    }
  }
}