
import pytest
from base.sincwise_geofence_metods import GeofenceADVEdit


class TestADVImages:
    geofence_list = [43977, 43978, 43979, 43980, 43981, 43982, 43983]
    data = None
    geofence_adv_edit = None

    @pytest.fixture(autouse=True)
    def check_command_for_geofence(self, signature_api_360):
        self.geofence_adv_edit = GeofenceADVEdit(signature_api_360.SECRET_KEY)
        self.data = [i for i in self.geofence_adv_edit.get_course_geofence_list() if i["id_geofence"] in self.geofence_list]

    def get_new_command(self, id_geofence, command):
        for i in self.data:
            if i["id_geofence"] == id_geofence:
                print(i)
                return i[command]

    def test_receive_adv_images(self):
        # 1 name
        old_name = self.get_new_command(self.geofence_list[0], "name")
        print(old_name)

        # 2 ON
        on = self.get_new_command(self.geofence_list[1], "status")
        print(on)

        #3 OFF
        off = self.get_new_command(self.geofence_list[2], "status")
        print(off)

        #4 visible
        visible = self.get_new_command(self.geofence_list[3], "visible")
        print(visible)

        #5 invisible
        invisible = self.get_new_command(self.geofence_list[4], "visible")
        print(invisible)










