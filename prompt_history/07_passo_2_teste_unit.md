Estamos no ciclo TDD para o Passo 2: validação e tratamento de alelos desconhecidos no Core.

Contexto:
A função 'get_allele_activity_score' em 'src/cyp2d6_classifier/core/activity_score.py' atualmente só trata alelos conhecidos (*1, *4, *10). Precisamos garantir que alelos inválidos ou não catalogados lancem uma exceção explícita.

Tarefa (Fase RED):
No arquivo 'tests/unit/test_activity_score.py', adicione uma nova função de teste unitário chamada 'test_get_allele_activity_score_unknown_allele_raises_error':
1. Use '@pytest.mark.unit'.
2. Siga o padrão AAA com comentários explícitos.
3. Use 'with pytest.raises(ValueError, match="Unknown or unsupported allele"): ...' para verificar que a chamada 'get_allele_activity_score("*99")' lança um 'ValueError' com mensagem descritiva.
4. Anote a tipagem estrita de retorno (-> None).

Atenção: Apenas modifique o arquivo de teste. Não altere o código em 'src/cyp2d6_classifier/core/activity_score.py' ainda. O teste deve falhar.