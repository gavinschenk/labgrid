import pytest
from labgrid.driver import SSHDriver, NoResourcError
from labgrid.resource import NetworkService


class TestSSHDriver:
    def test_create_fail_missing_resource(self, target):
        with pytest.raises(NoResourcError):
            SSHDriver(target)

    def test_create(self, target):
        target.add_resource(NetworkService())
        s = SSHDriver(target)
        assert(isinstance(s, SSHDriver))