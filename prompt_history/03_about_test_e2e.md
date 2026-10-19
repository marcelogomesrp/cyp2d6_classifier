Crie o arquivo tests/e2e/test_cli_e2e.py para validar a execução ponta a ponta (E2E) da CLI via linha de comando real.

Contexto do problema:
O teste unitário passou usando CliRunner em memória, mas a invocação real via terminal (`python -m cyp2d6_classifier.cli about`) não imprimiu nada na tela. Precisamos de um teste E2E que reproduza e capture essa falha real de processo.

Requisitos obrigatórios:
1. Siga estritamente as diretrizes do AGENTS.md.
2. Utilize o módulo 'subprocess' e 'sys.executable' para disparar o comando:
   [sys.executable, "-m", "cyp2d6_classifier.cli", "about"]
3. Capture a saída real do sistema operacional usando capture_output=True e text=True.
4. Marque o teste com o decorator @pytest.mark.e2e.
5. Utilize anotação de tipo explícita no retorno (-> None).
6. Estruture com comentários explícitos seguindo o padrão AAA (Arrange, Act, Assert).
7. Asserções requeridas:
   - result.returncode deve ser 0.
   - result.stdout deve conter "CYP2D6 Metabolizer Classifier".
   - result.stdout deve conter "CPIC Guidelines".

Não altere src/cyp2d6_classifier/cli.py ainda. Estamos estritamente na fase Red do teste E2E.