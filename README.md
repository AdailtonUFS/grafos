# Biblioteca de Grafos
## Disciplina: Grafos e Algoritmos Computacionais
### 2023.1 - Turma 01
### Dupla: Adailton Moura da Silva e Dean Vinicius Meneses Palmeira

Basicamente esse repositório trata-se da atividade da construção de uma biblioteca para lidar com grafos.

Como testar:

```shell
    git clone https://github.com/amskywalker/grafos.git
```

Para rodar no terminal certifique-se de configurar o PYTHONPATH

No linux:
```shell
    export PYTHONPATH="absolutepath/grafos:$PYTHONPATH"
    # certifique-se de mudar o absolutepath para o path no seu computador. 
```

No windows:
```shell
    setx PYTHONPATH "absolutepath\grafos;%PYTHONPATH%"
```

OBS: Caso esteja utilizando outro SO certifique-se de buscar como configurar a variavel PYTHONPATH

Rode o comando
```shell
    pip install -r requirements.txt
```

Entre na pasta do projeto e entre no diretorio principal
```shell
    cd graphs
```


então rode
```shell
    python main.py
```


Ao rodar o comando anterior serão acionadas as classes de exemplo e aparecerá a representação de dois grafos
no terminal