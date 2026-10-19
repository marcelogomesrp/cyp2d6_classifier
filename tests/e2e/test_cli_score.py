import pytest
from click.testing import CliRunner

from cyp2d6_classifier.cli import main as cli


@pytest.mark.e2e
def test_cli_score_success() -> None:
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(cli, ["score", "*1/*4"])

    # Assert
    assert result.exit_code == 0
    assert "Activity Score: 1.0" in result.output


@pytest.mark.e2e
def test_cli_score_unknown_allele() -> None:
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(cli, ["score", "*99/*1"])

    # Assert
    assert result.exit_code != 0
    assert "Error: Unknown or unsupported allele: *99" in result.output


@pytest.mark.e2e
def test_cli_score_invalid_format() -> None:
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(cli, ["score", "invalido"])

    # Assert
    assert result.exit_code != 0
    assert "Invalid diplotype format" in result.output
