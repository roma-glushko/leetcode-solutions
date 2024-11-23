class ValidParentheses:
    """
    Problem Link: https://leetcode.com/problems/valid-parentheses/
    Complexity: Easy

    Runtime: 28ms
    Memory: 14.5MB
    """

    openings: tuple[str, ...] = ("(", "[", "{")
    closing_map: dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    def isValid(self, s: str) -> bool:
        parentheses_stack: list[str] = []

        for parentheses in s:
            if parentheses in self.openings:
                # collect all opening parentheses
                parentheses_stack.append(parentheses)
                continue

            last_parentheses: str = (
                parentheses_stack[-1] if len(parentheses_stack) else ""
            )

            if (
                parentheses in self.closing_map
                and self.closing_map[parentheses] == last_parentheses
            ):
                # parentheses are matched, let remove this pair
                del parentheses_stack[-1]
                continue

            # parentheses are not matched

            return False

        if len(parentheses_stack) == 0:
            return True

        return False
