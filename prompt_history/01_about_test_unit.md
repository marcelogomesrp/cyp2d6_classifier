    Crie o arquivo tests/unit/test_cli.py para validar o comando 'about' da CLI.

    Requisitos obrigatórios:
    1. Siga estritamente as diretrizes do AGENTS.md.
    2. Utilize o CliRunner do click.testing para invocar o comando em memória a partir do entrypoint 'main' em cyp2d6_classifier.cli.
    3. Marque o teste com o decorator @pytest.mark.unit.
    4. Utilize anotação de tipo explícita no retorno (-> None).
    5. Estruture o teste com comentários explícitos seguindo o padrão AAA (Arrange, Act, Assert).
    6. Asserções requeridas:
    - result.exit_code deve ser 0.
    - result.output deve conter "CYP2D6 Metabolizer Classifier".
    - result.output deve conter "CPIC Guidelines".

    Não crie o arquivo de implementação src/cyp2d6_classifier/cli.py ainda. Estamos estritamente na fase Red do TDD.