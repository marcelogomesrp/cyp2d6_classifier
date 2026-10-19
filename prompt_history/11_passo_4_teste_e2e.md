Estamos no ciclo TDD para o Passo 4: exposição do cálculo de Activity Score via interface de linha de comando (CLI).

Contexto:
As regras de cálculo no Core já estão testadas e operacionais. Agora precisamos expor essa capacidade ao usuário final através de um novo subcomando na CLI chamado 'score'.

Tarefa (Fase RED):
Crie o arquivo de teste ponta a ponta 'tests/e2e/test_cli_score.py' utilizando o 'CliRunner' do Click:
1. Importe o grupo CLI principal a partir de 'cyp2d6_classifier.cli'.
2. Adicione o marcador '@pytest.mark.e2e'.
3. Crie os seguintes testes E2E seguindo o padrão AAA com tipagem estrita de retorno (-> None):
   - 'test_cli_score_success':
     * Executa: runner.invoke(cli, ["score", "*1/*4"])
     * Asserções: exit_code == 0 e "Activity Score: 1.0" presente em result.output.
   - 'test_cli_score_unknown_allele':
     * Executa: runner.invoke(cli, ["score", "*99/*1"])
     * Asserções: exit_code != 0 e mensagem de erro amigável presente em result.output (ex: "Error: Unknown or unsupported allele: *99").
   - 'test_cli_score_invalid_format':
     * Executa: runner.invoke(cli, ["score", "invalido"])
     * Asserções: exit_code != 0 e indicação de formato inválido presente em result.output.

Atenção: Apenas crie o arquivo de teste 'tests/e2e/test_cli_score.py'. Não altere 'src/cyp2d6_classifier/cli.py' ainda. O teste deve falhar (fase RED) indicando que o comando 'score' não existe no grupo CLI.