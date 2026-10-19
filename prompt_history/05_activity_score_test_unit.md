Estamos iniciando a modelagem do domínio clínico (Core) do classificador CYP2D6 via TDD.

Diretriz arquitetural obrigatória para esta tarefa:
- Toda a lógica de cálculo biológico deve pertencer estritamente à camada de domínio puro: 'src/cyp2d6_classifier/core/'.
- É expressamente proibido importar bibliotecas de CLI (como Click), manipular arquivos de disco diretamente ou realizar prints nesta camada.
- O código deve ser puramente funcional, determinístico e com tipagem estrita (MyPy).

Tarefa:
Crie o arquivo de teste unitário 'tests/unit/test_activity_score.py' para validar o cálculo do Activity Score (AS) de alelos individuais segundo as diretrizes do CPIC:
- Alelo '*1' (função normal) -> score 1.0
- Alelo '*4' (função nula) -> score 0.0
- Alelo '*10' (função reduzida) -> score 0.25

Requisitos do teste:
1. O teste deve importar a função 'get_allele_activity_score' a partir de 'cyp2d6_classifier.core.activity_score'.
2. Utilize '@pytest.mark.unit' e '@pytest.mark.parametrize' para cobrir os três casos de teste.
3. Anote explicitamente a tipagem de retorno do teste (-> None).
4. Siga o padrão AAA (Arrange, Act, Assert).

Atenção: Estamos na fase RED. Não crie o arquivo de implementação 'src/cyp2d6_classifier/core/activity_score.py' ainda. Apenas o arquivo de teste deve ser criado.