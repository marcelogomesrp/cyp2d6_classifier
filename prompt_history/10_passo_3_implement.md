Estamos na fase GREEN do ciclo TDD para o Passo 3: implementação do cálculo de Activity Score para diplotipos.

Contexto:
Os testes em 'tests/unit/test_activity_score.py' falham por erro de importação da função 'calculate_diplotype_activity_score'.

Tarefa:
No arquivo 'src/cyp2d6_classifier/core/activity_score.py', implemente e exporte a função 'calculate_diplotype_activity_score':

Requisitos obrigatórios:
1. Assinatura da função com tipagem estrita (MyPy):
   def calculate_diplotype_activity_score(diplotype: str) -> float:
2. Validação de formato:
   - Divida a string do diplotipo usando '/' como separador.
   - Caso a divisão não resulte em exatamente dois alelos (ou se algum dos alelos for vazio após remover espaços em branco), lance:
     ValueError(f"Invalid diplotype format: {diplotype}. Expected format '*allele1/*allele2'")
3. Reutilização de Domínio:
   - Para cada um dos dois alelos extraídos, utilize a função 'get_allele_activity_score' já existente.
   - Retorne a soma dos escores de ambos os alelos.
4. Respeite as diretrizes de arquitetura:
   - Zero dependência de CLI/Click, sem prints e sem I/O.
   - Código determinístico e puro.

Atenção: Faça apenas a implementação mínima e estritamente necessária para satisfazer os testes unitários.