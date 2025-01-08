"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=24 ; task=2)
"""

import sys
from itertools import chain


def swap(a: str, b: str, lookup: dict[str, str], reverse_lookup: dict[str, str]) -> bool:
    op1 = lookup[a]
    op2 = lookup[b]
    lookup[a], lookup[b] = op2, op1
    reverse_lookup[op1], reverse_lookup[op2] = reverse_lookup[op2], reverse_lookup[op1]


def main() -> None:
    # The input file implements a ripple-carry adder, a.k.a. multiple full adders to add N-bit numbers.
    # Refer to the `full_adder.gif` file in this folder for a graphical representation of the full adder and hence,
    # and for a better understanding of this solution.

    # Wires not needed since this is a generic solution
    _, joints = sys.stdin.read().strip().split("\n\n")
    gates = [tuple(joint.split(" -> ")) for joint in joints.splitlines()]
    pairs, num_z = [], sum(sol.startswith("z") for _, sol in gates)
    lookup = {output: joint for joint, output in gates}
    reverse_lookup = {v: k for k, v in lookup.items()}

    while len(pairs) < 4:  # This will detect one pair at a time
        # Lowest bit sum
        adder = reverse_lookup.get("x00 XOR y00", reverse_lookup.get("y00 XOR x00"))

        # Lowest bit carry
        carry = reverse_lookup.get("x00 AND y00", reverse_lookup.get("y00 AND x00"))

        for i in range(1, num_z):
            xi, yi, zi = f"x{i:02}", f"y{i:02}", f"z{i:02}"
            bit = reverse_lookup.get(f"{xi} XOR {yi}", reverse_lookup.get(f"{yi} XOR {xi}"))

            if adder := reverse_lookup.get(
                f"{bit} XOR {carry}",
                reverse_lookup.get(f"{carry} XOR {bit}"),
            ):
                # Adder detected, then let's calculate the next carry

                # First part of the carry
                c1 = reverse_lookup.get(f"{xi} AND {yi}", reverse_lookup.get(f"{yi} AND {xi}"))

                # Second part of the carry
                c2 = reverse_lookup.get(
                    f"{bit} AND {carry}",
                    reverse_lookup.get(f"{carry} AND {bit}"),
                )

                # Next carry
                carry = reverse_lookup.get(f"{c1} OR {c2}", reverse_lookup.get(f"{c2} OR {c1}"))

                if adder != zi:
                    # The final adder should be Zi, otherwise, we got an error and hence a swap.
                    pairs.append((adder, zi))
                    swap(adder, zi, lookup, reverse_lookup)
                    break  # Restart needed once a pair is found

            else:
                # No adder detected, so we need to swap the
                a, _, b = lookup[zi].split()
                n = a if a != carry else b
                pairs.append((bit, n))
                swap(bit, n, lookup, reverse_lookup)
                break  # Restart needed once a pair is found

    print(*sorted(chain.from_iterable(pairs)), sep=",")


if __name__ == "__main__":
    main()
