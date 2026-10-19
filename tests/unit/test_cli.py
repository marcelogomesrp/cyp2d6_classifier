import pytest
from click.testing import CliRunner

from cyp2d6_classifier.cli import main


@pytest.mark.unit
def test_about_command() -> None:
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(main, ["about"])

    # Assert
    assert result.exit_code == 0
    assert "CYP2D6 Metabolizer Classifier" in result.output
    assert "CPIC Guidelines" in result.output
