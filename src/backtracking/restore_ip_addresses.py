from typing import List


class RestoreIPAddresses:
    """
    Problem Link: https://leetcode.com/problems/restore-ip-addresses/
    Complexity: Medium
    Runtime: 32ms
    Memory: 14.2MB
    """
    def restoreIpAddresses(self, string: str) -> List[str]:
        ip_list: List[str] = []

        def is_valid_submask(submask: str) -> bool:
            if len(submask) > 1 and submask.startswith('0'):
                return False

            if int(submask) > 255:
                # outside of the range
                return False

            return True

        def search_ip_submask(ip_string: str, submask_start_idx: int, found_submasks: int) -> None:
            if found_submasks == 3:
                # we start from 0 submask, so there 0..3 submasks

                if not is_valid_submask(ip_string[submask_start_idx:]):
                    return

                ip_list.append(ip_string)

            # max possible submask number is 3 digit long (100-255)
            for submask_end_idx in range(submask_start_idx + 1, submask_start_idx + 4):
                if submask_end_idx >= len(ip_string):
                    return

                submask: str = ip_string[submask_start_idx:submask_end_idx]

                if not is_valid_submask(submask):
                    return

                search_ip_submask(
                    ip_string[:submask_end_idx] + '.' + ip_string[submask_end_idx:],
                    submask_end_idx + 1,
                    found_submasks + 1
                )

        search_ip_submask(string, 0, 0)

        return ip_list