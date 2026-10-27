# Registro do ciclo de TDD

Fui resolvendo um cenário por vez, rodando o pytest depois de cada alteração para ver se o teste falhava ou passava como esperado.

## Ciclo 1 - Taxa inicial

### Red
**Teste criado:** `test_taxa_inicial_ate_tres_km` (2 km, pedido de R$ 50, taxa de R$ 5).

**Motivo da falha:** a função `calcular_taxa_entrega` ainda não existia no arquivo `pedido.py`, então o pytest não conseguiu importar a função.

### Green
**Implementação realizada:** criei a função retornando 5, suficiente para atender ao primeiro teste. Rodei os testes antigos junto com o novo e passaram.

## Ciclo 2 - Quilômetro excedente

### Red
**Teste criado:** `test_acrescenta_taxa_por_km_excedente` (4 km, pedido de R$ 50, taxa de R$ 7).

**Motivo da falha:** a função ainda retornava 5. O teste esperava 7.

### Green
**Implementação realizada:** acrescentei R$ 2 por quilômetro acima dos 3 km. Executei a suíte toda de novo e os testes passaram.

## Ciclo 3 - Entrega gratuita

### Red
**Teste criado:** `test_entrega_gratuita_a_partir_de_cem_reais` (5 km, pedido de R$ 100, taxa de R$ 0).

**Motivo da falha:** sem a regra de gratuidade, o resultado era 9, mas deveria ser zero.

### Green
**Implementação realizada:** adicionei uma condição para retornar 0 quando o pedido for de R$ 100 ou mais. Os testes anteriores continuaram passando.

## Desafio opcional - Distância negativa

Também testei `test_rejeita_distancia_negativa`. Primeiro ele falhou porque a função aceitava valores negativos. Depois, adicionei `ValueError` para esse caso.

## Refactor

**Melhoria realizada:** simplifiquei o cálculo usando a variável `km_excedentes`, com `max(0, distancia_km - 3)`. Assim, a taxa fixa e a parte variável ficam no mesmo retorno, sem precisar de dois retornos para distância curta e longa.

**Resultado final:** os 8 testes passaram (4 testes que já vinham no projeto, 3 cenários obrigatórios e 1 opcional), sem regressões. O relatório da última execução está em `relatorio-testes.txt`.
