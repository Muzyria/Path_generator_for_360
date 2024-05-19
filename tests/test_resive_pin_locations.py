import pytest
from base.adb_commands import AdbCommands


class TestPinLocations:

    @pytest.fixture(autouse=True)
    def adb_command(self):
        adb_command = AdbCommands("192.168.0.105")
        adb_command.device_connect()

    @pytest.mark.parametrize("i", range(1, 2))
    def test_pin_locations(self, signature_api_360, i):
        print(signature_api_360.SECRET_KEY)
        # signature_api_360.pin_position_update()



