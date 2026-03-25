# Beam Reaction Calculator
# Calculates support reactions for a simply supported beam with point loads

from typing import List, Tuple


def calculate_reactions(span: float, loads: List[Tuple[float, float]]) -> Tuple[float, float]:
    """
    Calculate reactions at supports A and B for a simply supported beam.

    Parameters:
        span: Length of the beam
        loads: List of (force, position) tuples

    Returns:
        (Ay, By): reactions at supports A and B
    """
    total_load = sum(force for force, _ in loads)
    moment_about_a = sum(force * position for force, position in loads)

    by = moment_about_a / span
    ay = total_load - by

    return ay, by


def display_results(span: float, loads: List[Tuple[float, float]], ay: float, by: float) -> None:
    print("\nBEAM REACTION CALCULATOR")
    print("-" * 40)
    print(f"Beam span: {span:.2f} m")
    print("\nApplied Loads:")
    for i, (force, position) in enumerate(loads, start=1):
        print(f"  Load {i}: {force:.2f} N at x = {position:.2f} m")

    print("\nSupport Reactions:")
    print(f"  Reaction at A: {ay:.2f} N")
    print(f"  Reaction at B: {by:.2f} N")


def main() -> None:
    span = 10.0
    loads = [
        (500.0, 2.0),
        (800.0, 5.0),
        (300.0, 8.0),
    ]

    ay, by = calculate_reactions(span, loads)
    display_results(span, loads, ay, by)


if __name__ == "__main__":
    main()
