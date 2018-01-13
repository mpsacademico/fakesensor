# FakeSensor

FakeSensor é uma boa maneira de simular um sensor que produz arquivos de dados.  
Em pipelines em que a entrada de dados é baseada em sensores, alguns desafios podem ocorrer:

- a falta de acesso aos dados reais desde o início do projeto
- o ambiente de desenvolvimento não tem acesso aos dados produzidos
- a simulação de diferentes configurações de sensor sem interência no operacional

## Como executar?

Em um terminal do UNIX, executar o seguinte comando:

```
./fks.py run
```

### Parâmetros

`run` - executar a aplicação
