# como executar

primeiro, é necessário clonar o repositório em sua maquina, use o comando git clone em seu terminal

```
git clone https://github.com/Joao-Lucas-Si/2026-sprint2-python.git
```

depois entre na pasta do projeto e crie um ambiente python

```
cd sprint2-python

python -m venv venv
```

ative o ambiente python e instale as depêndencias

```
source venv/bin/activate

cd back

pip install -r requirements.txt

cd ../front/user

pip install -r requirements.txt
```

agora, será necessário ter dois terminais, no primerio terminal, o que você já esta utilizando, rode o script do frontend, já no segundo, ative o ambiente python e entre na pasta back e rode o backend


## primerio terminal

ao rodar o comando de ativação do frontend, tenha em mente que será aberto um aplicativo desktop em sua maquina, esse protótipo foi feito com o mobile em mente, e o desktop e web só será foco no futuro do projeto para a versão admin do aplicativo, mas para testes e execução simples do aplicativo de usuário, o desktop servirá
```
flet run main.py
```

## segundo terminal

```
source venv/bin/activate

cd back

python main.py
```

