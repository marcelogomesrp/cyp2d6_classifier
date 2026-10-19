Estamos na fase GREEN do ciclo TDD para o Passo 2: tratamento de alelos desconhecidos no Core.

Contexto:
O teste unitário 'test_get_allele_activity_score_unknown_allele_raises_error' em 'tests/unit/test_activity_score.py' falha porque a função ainda não valida entradas não catalogadas.

Tarefa:
Atualize o arquivo 'src/cyp2d6_classifier/core/activity_score.py':
1. Altere a função 'get_allele_activity_score' para lançar 'ValueError(f"Unknown or unsupported allele: {allele}")' quando o alelo informado não estiver presente no mapeamento de alelos suportados (*1, *4, *10).
2. Mantenha as diretrizes de isolamento do Core (zero dependência de CLI/Click, sem I/O e sem prints).
3. Mantenha as anotações de tipagem estrita (MyPy).

Atenção: Não adicione novos alelos ou lógicas desnecessárias neste momento. Apenas garanta que o mapeamento existente continue funcionando e que alelos desconhecidos lancem o ValueError esperado.