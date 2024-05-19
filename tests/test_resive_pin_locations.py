
from base.sincwise_clients_method import SyncwiseClient


class TestPinLocations:

    data = SyncwiseClient("https://api2.syncwise360.com")

    def test_pin_locations(self):
        print(self.data)


