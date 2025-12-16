"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=10 ; task=1)
"""

import sys
from collections import deque


def main() -> None:
    ans = 0
    for line in sys.stdin:
        config = line.strip().split()

        # Convert target lights to bitmask: .=0 ; #=1
        # Example: [.##.] -> bits: 0110 (binary) -> 6 (decimal)
        target = sum(1 << i for i, v in enumerate(config[0][1:-1]) if v == "#")

        # Convert each button to a bitmask of lights it toggles
        # Example: (1,3) -> bits at positions 1 and 3 set to 1 -> 1010 (binary) -> 10 (decimal)
        btns = [sum(1 << i for i in map(int, btn[1:-1].split(","))) for btn in config[1:-1]]

        # BFS to find shortest sequence of button presses
        # Start with all lights off (cur_node = 0)
        checked = {0}  # Track visited states to avoid cycles
        q = deque([(0, 0)])  # (current state, number of presses)
        while q:
            cur_node, btn_presses = q.popleft()

            if cur_node == target:
                ans += btn_presses
                break  # Found minimal presses for this machine, since this is BFS :)

            # Try pressing each button from current state
            for btn in btns:
                # XOR toggles bits: 0^1=1 (turns on), 1^1=0 (turns off)
                # So XOR simulates pressing the buttons: light on (bit 1) -> light off (bit 0) and viceversa
                if (next_node := (cur_node ^ btn)) not in checked:
                    checked.add(next_node)
                    q.append((next_node, btn_presses + 1))

    print(ans)


if __name__ == "__main__":
    main()
