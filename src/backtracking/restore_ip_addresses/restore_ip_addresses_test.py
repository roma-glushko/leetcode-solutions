from unittest import TestCase

from .restore_ip_addresses import RestoreIPAddresses


class RestoreIPAddressesTest(TestCase):
    def test_default_inputs(self):
        solution = RestoreIPAddresses()

        self.assertCountEqual(
            ["255.255.11.135", "255.255.111.35"],
            solution.restoreIpAddresses("25525511135"),
        )

        self.assertCountEqual(
            ["0.0.0.0"],
            solution.restoreIpAddresses("0000"),
        )

        self.assertCountEqual(
            ["1.1.1.1"],
            solution.restoreIpAddresses("1111"),
        )

        self.assertCountEqual(
            ["0.10.0.10", "0.100.1.0"],
            solution.restoreIpAddresses("010010"),
        )

        self.assertCountEqual(
            ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"],
            solution.restoreIpAddresses("101023"),
        )

    def test_no_valid_inputs(self):
        solution = RestoreIPAddresses()

        self.assertCountEqual(
            [],
            solution.restoreIpAddresses("0011255245"),
        )

        self.assertCountEqual(
            [],
            solution.restoreIpAddresses("000256"),
        )
