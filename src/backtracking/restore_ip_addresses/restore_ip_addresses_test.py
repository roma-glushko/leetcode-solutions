from .restore_ip_addresses import RestoreIPAddresses


def test_default_inputs():
    solution = RestoreIPAddresses()
    assert sorted(solution.restoreIpAddresses("25525511135")) == sorted(
        ["255.255.11.135", "255.255.111.35"]
    )
    assert sorted(solution.restoreIpAddresses("0000")) == sorted(["0.0.0.0"])
    assert sorted(solution.restoreIpAddresses("1111")) == sorted(["1.1.1.1"])
    assert sorted(solution.restoreIpAddresses("010010")) == sorted(
        ["0.10.0.10", "0.100.1.0"]
    )
    assert sorted(solution.restoreIpAddresses("101023")) == sorted(
        ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    )


def test_no_valid_inputs():
    solution = RestoreIPAddresses()
    assert sorted(solution.restoreIpAddresses("0011255245")) == sorted([])
    assert sorted(solution.restoreIpAddresses("000256")) == sorted([])
