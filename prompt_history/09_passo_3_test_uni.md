Estamos no ciclo TDD para o Passo 3: cálculo do Activity Score total de diplotipos no Core.

Contexto:
Temos 'get_allele_activity_score' testada e validada. Agora precisamos da função 'calculate_diplotype_activity_score' que recebe a string de um diplotipo (ex: '*1/*4'), extrai os dois alelos e retorna a soma dos seus escores segundo o CPIC.

Tarefa (Fase RED):
No arquivo 'tests/unit/test_activity_score.py', adicione uma nova bateria de testes unitários:
1. Importe 'calculate_diplotype_activity_score' a partir de 'cyp2d6_classifier.core.activity_score'.
2. Crie a função de teste 'test_calculate_diplotype_activity_score':
   - Anote com '@pytest.mark.unit' e '@pytest.mark.parametrize'.
   - Cubra os seguintes cenários:
     * diplotipo '*1/*1' -> score esperado 2.0 (1.0 + 1.0)
     * diplotipo '*1/*4' -> score esperado 1.0 (1.0 + 0.0)
     * diplotipo '*4/*4' -> score esperado 0.0 (0.0 + 0.0)
     * diplotipo '*1/*10' -> score esperado 1.25 (1.0 + 0.25)
   - Siga o padrão AAA com comentários explícitos.
   - Anote a tipagem estrita de retorno (-> None).
3. Crie a função de teste 'test_calculate_diplotype_activity_score_invalid_format_raises_error':
   - Valide que passar formatos que não contenham exatamente dois alelos separados por '/' (ex: '*1', '*1/*4/*4', 'invalid') lance 'ValueError'.

Atenção: Apenas adicione os testes ao arquivo 'tests/unit/test_activity_score.py'. Não crie nem altere a implementação em 'src/cyp2d6_classifier/core/activity_score.py' ainda. O teste deve falhar (ImportError/AttributeError).