# Diretrizes para o Agente de Desenvolvimento (AGENTS.md)

## 1. Contexto do Domínio
- Módulo determinístico para classificação do fenótipo metabolizador da enzima CYP2D6 baseado nas diretrizes clínicas do CPIC.
- Rigor e determinismo clínico são inegociáveis.

## 2. Padrões de Código e Arquitetura
- Python 3.11+ utilizando Poetry.
- Type Hints estritos em todas as assinaturas de funções e retornos.
- Proibido o uso de inferências probabilísticas ou chamadas de LLM em tempo de execução para regras de negócio ou cálculos de escore.
- Respeite rigorosamente as exclusões de `.agyignore` e `.gitignore`. Nunca inspecione diretórios de cache (`.pytest_cache/`, `cov_*/`, `.venv/`).

### Separação de Camadas (Arquitetura)
- **Camada Core (`src/cyp2d6_classifier/core/`)**:
  - Contém toda a lógica de domínio biológico e diretrizes do CPIC (alelos, escores, fenótipos).
  - Código puramente funcional e determinístico, com tipagem estrita (MyPy).
  - Proibido importar bibliotecas de CLI (Click), manipular arquivos de disco diretamente ou realizar prints.
- **Camada de Interface (`src/cyp2d6_classifier/cli.py`)**:
  - Ponto de entrada exclusivo para interação via linha de comando (Click).
  - Responsável apenas por parsing de argumentos, formatação de saída e códigos de retorno no terminal.
  - Toda a inteligência clínica DEVE ser delegada para a camada `core`.

## 3. Protocolo de Testes (Pytest)
- Framework: `pytest` com `pytest-cov`.
- Testes unitários devem residir em `tests/unit/`.
- Testes ponta a ponta (E2E) devem residir em `tests/e2e/` e utilizar a marker `@pytest.mark.e2e`.
- Siga estritamente o padrão AAA (Arrange, Act, Assert) com comentários explícitos.
- Use `@pytest.mark.parametrize` para matrizes de diplotipos e alelos.
- Cubra caminhos felizes, fronteiras de corte (< vs <=) e exceções (`pytest.raises(ValueError)`).

## 4. Comandos de Validação Permitidos
- Testes unitários: `task test:unit` (ou `poetry run pytest tests/unit`)
- Testes E2E: `task test:e2e` (ou `poetry run pytest tests/e2e`)
- Suíte completa: `task test:all`
- Quality Gate (Lint, Tipagem e Testes): `task check`
- Relatório de cobertura: `task test_cov`