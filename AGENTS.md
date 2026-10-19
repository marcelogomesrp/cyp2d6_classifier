# Diretrizes para o Agente de Desenvolvimento (AGENTS.md)

## 1. Contexto do Domínio
- Módulo determinístico para classificação do fenótipo metabolizador da enzima CYP2D6 baseado nas diretrizes clínicas do CPIC.
- Rigor e determinismo clínico são inegociáveis.

## 2. Padrões de Código e Arquitetura
- Python 3.11+ utilizando Poetry.
- Type Hints estritos em todas as assinaturas de funções e retornos.
- Proibido o uso de inferências probabilísticas ou chamadas de LLM em tempo de execução para regras de negócio ou cálculos de escore.
- Respeite rigorosamente as exclusões de `.agyignore` e `.gitignore`. Nunca inspecione diretórios de cache (`.pytest_cache/`, `cov_*/`, `.venv/`).

## 3. Protocolo de Testes (Pytest)
- Framework: `pytest` com `pytest-cov`.
- Testes unitários devem residir em `tests/unit/`.
- Siga estritamente o padrão AAA (Arrange, Act, Assert) com comentários explícitos.
- Use `@pytest.mark.parametrize` para matrizes de diplotipos.
- Cubra caminhos felizes, fronteiras de corte (< vs <=) e exceções (`pytest.raises(ValueError)`).

## 4. Comandos de Validação Permitidos
- Testes unitários: `poetry run pytest tests/unit`
- Relatório de cobertura: `poetry run pytest tests/unit --cov=cyp2d6_classifier --cov-report=term-missing`