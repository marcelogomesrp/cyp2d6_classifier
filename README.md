# CYP2D6 Metabolizer Classifier

> Módulo determinístico e auditável para classificação do fenótipo metabolizador da enzima CYP2D6, baseado nas diretrizes clínicas do CPIC (Clinical Pharmacogenetics Implementation Consortium).

---

## 🎯 Sobre o Projeto

Este repositório foi construído com foco em **reprodutibilidade estrita, tipagem rigorosa e TDD (Test-Driven Development)**, servindo tanto para o uso em pipelines bioinformáticos quanto como referência para integração determinística com agentes de Inteligência Artificial.

- **Sem caixa-preta:** Regras de negócio e conversões de escore de atividade baseadas em diretrizes clínicas abertas.
- **Rigor de Qualidade:** Esteira automatizada de testes, linting estático e verificação de tipos.

---

## 🛠️ Stack Tecnológica & Requisitos

- **Python:** `>=3.11,<4.0` (gerenciado via `pyenv`)
- **Gerenciador de Dependências:** `poetry`
- **Automação de Tarefas:** `taskipy`
- **Qualidade de Código:** `ruff` (Linter/Formatter) & `mypy` (Type Checking)
- **Testes:** `pytest`, `pytest-cov` & `pytest-mock`

---

## 🚀 Setup Rápido para Desenvolvimento

Siga os passos abaixo para clonar e preparar o ambiente de desenvolvimento na sua máquina:

### 1. Clonar o Repositório
```bash
git clone [https://github.com/marcelogomesrp/cyp2d6_classifier.git](https://github.com/marcelogomesrp/cyp2d6_classifier.git)
cd cyp2d6_classifier