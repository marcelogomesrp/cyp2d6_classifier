import pytest

from cyp2d6_classifier.core.activity_score import (
    calculate_diplotype_activity_score,
    get_allele_activity_score,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("allele", "expected_score"),
    [
        ("*1", 1.0),
        ("*4", 0.0),
        ("*10", 0.25),
    ],
)
def test_get_allele_activity_score_returns_cpic_score(
    allele: str, expected_score: float
) -> None:
    # Arrange
    target_allele: str = allele

    # Act
    actual_score: float = get_allele_activity_score(target_allele)

    # Assert
    assert actual_score == expected_score


@pytest.mark.unit
def test_get_allele_activity_score_unknown_allele_raises_error() -> None:
    # Arrange
    unknown_allele: str = "*99"

    # Act & Assert
    with pytest.raises(ValueError, match="Unknown or unsupported allele"):
        get_allele_activity_score(unknown_allele)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("diplotype", "expected_score"),
    [
        ("*1/*1", 2.0),
        ("*1/*4", 1.0),
        ("*4/*4", 0.0),
        ("*1/*10", 1.25),
    ],
)
def test_calculate_diplotype_activity_score(
    diplotype: str, expected_score: float
) -> None:
    # Arrange
    target_diplotype: str = diplotype

    # Act
    actual_score: float = calculate_diplotype_activity_score(target_diplotype)

    # Assert
    assert actual_score == expected_score


@pytest.mark.unit
@pytest.mark.parametrize(
    "invalid_diplotype",
    [
        "*1",
        "*1/*4/*4",
        "invalid",
    ],
)
def test_calculate_diplotype_activity_score_invalid_format_raises_error(
    invalid_diplotype: str,
) -> None:
    # Arrange
    target_diplotype: str = invalid_diplotype

    # Act & Assert
    with pytest.raises(ValueError):
        calculate_diplotype_activity_score(target_diplotype)
