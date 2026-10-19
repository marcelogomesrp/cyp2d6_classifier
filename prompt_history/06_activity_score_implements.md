## Arquitetura e Organização de Código

O projeto adota uma separação estrita de responsabilidades:

1. **Camada Core (`src/cyp2d6_classifier/core/`)**:
   - Contém toda a lógica biológica e regras do CPIC (alelos, escores, fenótipos).
   - Código puramente funcional e determinístico, com tipagem estrita (MyPy).
   - Proibido importar bibliotecas de CLI (Click), manipular arquivos de disco diretamente ou realizar prints.

2. **Camada de Interface (`src/cyp2d6_classifier/cli.py`)**:
   - Responsável exclusiva pelo parsing de argumentos, formatação de saída e códigos de retorno no terminal.
   - Toda a inteligência clínica DEVE ser delegada para a camada `core`.