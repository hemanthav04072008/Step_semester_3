class Candidate:
    def __init__(self, name, cgpa, coding_score):
        self.name = name
        self.cgpa = cgpa
        self.coding_score = coding_score
        self.composite_score = cgpa * 10 + coding_score * 0.5

    @staticmethod
    def is_eligible(cgpa, coding_score=None):
        if coding_score is None:
            return cgpa >= 7.5

        return (
            cgpa >= 7.5
            or (cgpa >= 6.5 and coding_score >= 60)
        )

    def __lt__(self, other):
        # Sort by composite score in descending order
        return self.composite_score > other.composite_score


def shortlist_and_rank(candidates):
    shortlisted = []

    for candidate in candidates:
        if Candidate.is_eligible(
            candidate.cgpa, candidate.coding_score
        ):
            shortlisted.append(candidate)

    ranked = sorted(shortlisted)

    if not ranked:
        return "No candidates shortlisted"

    result = []

    for i, candidate in enumerate(ranked, start=1):
        result.append(
            f"{i}. {candidate.name} "
            f"({candidate.composite_score:.1f})"
        )

    return " | ".join(result)


candidates = [
    Candidate("Aisha", 8.2, 40),
    Candidate("Rohit", 6.8, 65),
    Candidate("Meena", 6.0, 90),
    Candidate("Karan", 7.5, 20)
]

print(shortlist_and_rank(candidates))