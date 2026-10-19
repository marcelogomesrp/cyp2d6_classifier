import subprocess
import sys

import pytest


@pytest.mark.e2e
def test_cli_about_e2e() -> None:
    # Arrange
    command = [sys.executable, "-m", "cyp2d6_classifier.cli", "about"]

    # Act
    result = subprocess.run(command, capture_output=True, text=True)

    # Assert
    assert result.returncode == 0
    assert "CYP2D6 Metabolizer Classifier" in result.stdout
    assert "CPIC Guidelines" in result.stdout
