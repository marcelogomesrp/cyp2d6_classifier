def get_allele_activity_score(allele: str) -> float:
    scores: dict[str, float] = {
        "*1": 1.0,
        "*4": 0.0,
        "*10": 0.25,
    }
    if allele not in scores:
        raise ValueError(f"Unknown or unsupported allele: {allele}")
    return scores[allele]


def calculate_diplotype_activity_score(diplotype: str) -> float:
    parts: list[str] = [part.strip() for part in diplotype.split("/")]
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError(
            f"Invalid diplotype format: {diplotype}. "
            "Expected format '*allele1/*allele2'"
        )
    allele1, allele2 = parts[0], parts[1]
    return get_allele_activity_score(allele1) + get_allele_activity_score(allele2)
