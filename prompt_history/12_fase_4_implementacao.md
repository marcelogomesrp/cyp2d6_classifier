Estamos na fase GREEN do ciclo TDD para o Passo 4: implementação do comando 'score' na CLI.

Contexto:
Os testes em 'tests/e2e/test_cli_score.py' falham porque o subcomando 'score' ainda não foi registrado no grupo CLI principal.

Tarefa:
No arquivo 'src/cyp2d6_classifier/cli.py':
1. Importe a função 'calculate_diplotype_activity_score' a partir de 'cyp2d6_classifier.core.activity_score'.
2. Adicione o subcomando 'score' ao grupo 'cli' usando Click:
   - Receba o argumento obrigatório 'diplotype' como string (ex: @click.argument("diplotype", type=str)).
   - Dentro de um bloco try/except:
     * Chame 'calculate_diplotype_activity_score(diplotype)'.
     * Em caso de sucesso, exiba no terminal: f"Activity Score: {score}" (usando click.echo).
     * Se capturar 'ValueError' vindo do Core, exiba uma mensagem amigável no stderr via click.echo(f"Error: {e}", err=True) e encerre a execução com código de saída não-zero (ctx.exit(1) ou sys.exit(1)).
3. Mantenha as anotações estritas de tipagem (MyPy).

Atenção: A CLI não deve conter regras de cálculo. Ela deve apenas capturar o input, chamar o Core e imprimir o resultado ou erro amigável.