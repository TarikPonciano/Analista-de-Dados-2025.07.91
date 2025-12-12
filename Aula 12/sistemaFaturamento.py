'''
SISTEMA DE ANÁLISE DE FATURAMENTO SEMESTRAL
Versão: 3.0 (Implementação Incremental)

==================================================
FASE 1: IMPLEMENTAÇÃO BÁSICA
==================================================
OBJETIVOS:
1. Solicitar o faturamento dos 6 primeiros meses (Janeiro a Junho)
2. Validar se cada valor está entre R$ 5.000,00 e R$ 200.000,00
3. Calcular e exibir:
   - Total de faturamento no semestre
   - Faturamento médio mensal
   - Maior valor de faturamento (apenas o valor)
   - Menor valor de faturamento (apenas o valor)

INSTRUÇÕES:
- Use uma lista para armazenar os 6 valores
- Se o usuário digitar um valor fora do intervalo, peça novamente
- Formate os resultados monetários com 2 casas decimais

EXEMPLO DE SAÍDA (FASE 1):
=== ENTRADA DE FATURAMENTO ===
Faturamento de Janeiro (R$ 5000 a 200000): 15000
Faturamento de Fevereiro (R$ 5000 a 200000): 18000
...
=== RESULTADOS BÁSICOS ===
Total de faturamento: R$ 105000.00
Faturamento médio: R$ 17500.00
Maior faturamento: R$ 20000.00
Menor faturamento: R$ 15000.00

==================================================
FASE 2: HISTÓRICO E IDENTIFICAÇÃO DE MESES
==================================================
OBJETIVOS:
1. Manter todas as funcionalidades da FASE 1
2. Exibir um histórico mostrando mês e faturamento
3. Identificar e exibir o NOME do mês com maior faturamento
4. Identificar e exibir o NOME do mês com menor faturamento

INSTRUÇÕES:
- Crie uma lista: meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
- Modifique a exibição para mostrar o histórico
- Encontre os índices dos valores máximo e mínimo para obter os nomes dos meses

EXEMPLO DE SAÍDA (FASE 2):
=== HISTÓRICO DE FATURAMENTO ===
Janeiro: R$ 15000.00
Fevereiro: R$ 18000.00
...
=== RESUMO COMPLETO ===
Total de faturamento: R$ 105000.00
Faturamento médio: R$ 17500.00
Maior faturamento: R$ 20000.00 (Março)
Menor faturamento: R$ 15000.00 (Janeiro)

==================================================
FASE 3: CÁLCULO DE IMPOSTOS
==================================================
OBJETIVOS:
1. Manter todas as funcionalidades das FASES 1 e 2
2. Perguntar a porcentagem de imposto pago
3. Validar que a porcentagem não é negativa
4. Calcular e exibir:
   - Total de impostos pagos no semestre
   - Faturamento líquido (total - impostos)

INSTRUÇÕES:
- Após mostrar o resumo, peça: "Informe a porcentagem de imposto (%): "
- Valide se o valor não é negativo
- Calcule: impostos = total * (porcentagem/100)
- Calcule: líquido = total - impostos

EXEMPLO DE SAÍDA (FASE 3):
Informe a porcentagem de imposto (%): 15
=== RESUMO COM IMPOSTOS ===
Total de faturamento: R$ 105000.00
Total de impostos pagos: R$ 15750.00
Faturamento líquido: R$ 89250.00

==================================================
FASE 4: CLASSIFICAÇÃO POR DESEMPENHO
==================================================
OBJETIVOS:
1. Manter todas as funcionalidades das FASES 1, 2 e 3
2. Classificar cada mês em uma das três categorias:
   - FATURAMENTO ALTO: valor ≥ 120% da média
   - FATURAMENTO MÉDIO: valor entre 80% e 119% da média
   - FATURAMENTO BAIXO: valor < 80% da média
3. Contar e exibir quantos meses estão em cada categoria

INSTRUÇÕES:
- Use a média calculada na FASE 1
- Percorra a lista de faturamentos e classifique cada mês
- Use três variáveis contadoras: alto, medio, baixo
- Adicione a exibição dessas contagens ao final

EXEMPLO DE SAÍDA (FASE 4):
=== CLASSIFICAÇÃO POR DESEMPENHO ===
Meses com faturamento alto: 2
Meses com faturamento médio: 3
Meses com faturamento baixo: 1

==================================================
REGRAS GERAIS:
==================================================
1. Intervalo de entrada: R$ 5.000,00 a R$ 200.000,00
2. Porcentagem de imposto: não pode ser negativa
3. Formatação: todos os valores monetários com 2 casas decimais
4. Meses: Janeiro, Fevereiro, Março, Abril, Maio, Junho

==================================================
SEQUÊNCIA DE DESENVOLVIMENTO:
==================================================
1. Implemente e teste completamente a FASE 1
2. Quando funcionar, avance para a FASE 2
3. Depois implemente a FASE 3
4. Finalize com a FASE 4
5. Mantenha todas as funcionalidades anteriores ao avançar
'''