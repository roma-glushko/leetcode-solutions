from typing import List


class StringCompress:
    # Problem Link: https://leetcode.com/problems/string-compression/

    def compress(self, chars: List[str]) -> int:
        current_idx: int = 0
        write_idx: int = 0
        length: int = len(chars)

        while current_idx < length:
            sequence_start_idx: int = current_idx

            while current_idx < length and chars[current_idx] == chars[sequence_start_idx]:
                # try to reach the end of the sequence group explicitly
                current_idx += 1

            # encode the group
            chars[write_idx] = chars[sequence_start_idx]
            write_idx += 1

            sequence_len: int = current_idx - sequence_start_idx

            if sequence_len == 1:
                # skip sequences of length one to keep encoded string shorter
                continue

            for char in str(sequence_len):
                # encode group length
                chars[write_idx] = char
                write_idx += 1

        return write_idx
