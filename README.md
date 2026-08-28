# como executar

primeiro, é necessário clonar o repositório em sua maquina, use o comando git clone em seu terminal

```
git clone https://github.com/Joao-Lucas-Si/2026-sprint2-python.git
```

depois entre na pasta do projeto e crie um ambiente python

```
cd 2026-sprint2-python

python -m venv venv
```

ative o ambiente python se atentando ao sistema operacioanl usado, e instale as depêndencias

```
# para linux
source venv/bin/activate
# para wnindows
./venv/Scripts/Activate.ps1

cd back

pip install -r requirements.txt

cd ../front/user

pip install -r requirements.txt
```

agora, será necessário ter quatro terminais, no primerio terminal, o que você já esta utilizando, rode o script do frontend, já no segundo, ative o ambiente python e entre na pasta back e rode o backend


## primerio terminal

ao rodar o comando de ativação do frontend, tenha em mente que será aberto um aplicativo desktop em sua maquina, esse protótipo foi feito com o mobile em mente, e o desktop e web só será foco no futuro do projeto para a versão admin do aplicativo, mas para testes e execução simples do aplicativo de usuário, o desktop servirá
```
flet run main.py
```

## segundo terminal

```
# para linux
source venv/bin/activate
# para wnindows
./venv/Scripts/Activate.ps1

cd back

python main.py
```

## terceiro terminal

agora, o terceiro e quarto terminal serão voltados para rodar o hardware do carregador, fora os aspectos relacionados a terminal, tenha a extensão do wokwi instalada em seu vscode, agora, neste, o terceiro, ative o ambiente python, e entre na pastas hardware/Wokwi e instale o platformio

```
# para linux
source venv/bin/activate
# para wnindows
./venv/Scripts/Activate.ps1

cd hardware/Wokwi

pip install platformio
```

com o platformio instalado, crie o hardware com o seguinte comando

```
pio run
```

quando o comando finalizar, abra o arquivo diagram.json dentro da pasta hardware/Wokwi, isso abrirá a extensão do wokwi, que solicitará para você fazer login em seu site, faça o login para conseguir a licença de uso e depois volte para o vscode


## quarto terminal

o quarto terminal serve para rodar um intermediario que fará comunicação entre o wokwi e seu computador, basta entrar na pasta hardware/Wokwi/intermediarios e rodar o arquivo correspondente ao seu sistema operacional

```

cd hardware/Wokwi/intermediarios


# para linux

./wokwigw-linux

# para windows

./wokwigw.exe
```

agora, com o intermediario rodando, entre no arquvio diagram.json e rode o hardware