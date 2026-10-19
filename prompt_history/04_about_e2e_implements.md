Estamos na fase GREEN do ciclo TDD para o teste de ponta a ponta (E2E) da CLI.

Contexto:
O teste E2E em tests/e2e/test_cli_e2e.py falha porque a execução direta do módulo via subprocesso não dispara a CLI.
Além disso, o executável de console foi configurado em [project.scripts] como 'cyp2d6-classifier' apontando para 'cyp2d6_classifier.cli:main'.

Tarefas necessárias em src/cyp2d6_classifier/cli.py:
1. Siga estritamente as diretrizes do AGENTS.md e garanta tipagem estrita com MyPy.
2. Mantenha o grupo principal 'main' e o comando 'about' existentes.
3. Adicione a cláusula de execução direta do interpretador:
   if __name__ == "__main__":
       main()
4. Não adicione dependências extras ou lógica além do necessário para tornar o teste E2E verde.