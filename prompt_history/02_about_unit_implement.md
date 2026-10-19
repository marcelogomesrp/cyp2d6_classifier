Estamos na fase GREEN do TDD para o comando 'about' da CLI.

O teste tests/unit/test_cli.py já existe e está falhando por falta do módulo.

Implemente a solução mínima necessária no arquivo src/cyp2d6_classifier/cli.py:
1. Siga as diretrizes de tipagem estrita do AGENTS.md.
2. Utilize o Click para definir o grupo principal 'main' e o subcomando 'about'.
3. O comando 'about' deve imprimir exatamente as informações esperadas pelo teste ("CYP2D6 Metabolizer Classifier" e "CPIC Guidelines").
4. Não adicione dependências extras ou lógica além do estritamente necessário para tornar o teste verde.