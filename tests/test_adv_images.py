import os
import pytest
from base.sincwise_geofence_metods import GeofenceADVEdit


class TestADVImages:
    geofence_list = [43977, 43978, 43979, 43980, 43981, 43982, 43983]
    data = None
    geofence_adv_edit = None

    points_1 = [{'lat': '50.0804874', 'lng': '36.2319472'}, {'lat': '50.0803489', 'lng': '36.2327747'}, {'lat': '50.0801414', 'lng': '36.2326875'}, {'lat': '50.0802774', 'lng': '36.2318212'}]
    points_2 = [{'lat': '50.0804874', 'lng': '36.2319472'}, {'lat': '50.0802964', 'lng': '36.2321484'}, {'lat': '50.0801414', 'lng': '36.2326875'}, {'lat': '50.0802774', 'lng': '36.2318212'}]


    @pytest.fixture(autouse=True)
    def check_command_for_geofence(self, signature_api_360):
        self.geofence_adv_edit = GeofenceADVEdit(signature_api_360.SECRET_KEY)
        self.data = [i for i in self.geofence_adv_edit.get_course_geofence_list() if i["id_geofence"] in self.geofence_list]
        # for i in self.data:
        #     print(i)

    def get_new_command(self, id_geofence, command):
        for i in self.data:
            if i["id_geofence"] == id_geofence:
                # print(i)
                return i[command]

    def swap_file_names(self, directory_path="tests/images"):
        """
        Меняет имена двух файлов в указанной директории.

        :param directory_path: Путь к директории с двумя файлами.
        """
        try:
            # Получаем список файлов в директории
            files = os.listdir(directory_path)
            # Полный путь к каждому файлу
            file1 = os.path.join(directory_path, files[0])
            file2 = os.path.join(directory_path, files[1])
            # Создаем временные имена для обмена
            temp_name1 = os.path.join(directory_path, 'temp_file1.tmp')
            temp_name2 = os.path.join(directory_path, 'temp_file2.tmp')
            # Переименовываем файлы для временного хранения
            os.rename(file1, temp_name1)
            os.rename(file2, temp_name2)
            # Меняем местами файлы, используя оригинальные имена
            os.rename(temp_name1, file2)
            os.rename(temp_name2, file1)

            print("Имена файлов успешно обменены.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


    def test_receive_adv_images(self):
        # 1 name
        old_name = self.get_new_command(self.geofence_list[0], "name")
        # print(old_name)
        if old_name == "new_name_1":
            self.geofence_adv_edit.change_name(self.geofence_list[0], "new_name_2")
        else:
            self.geofence_adv_edit.change_name(self.geofence_list[0], "new_name_1")

        # 2 ON
        on = self.get_new_command(self.geofence_list[1], "status")
        # print(on)
        if on == 1:
            self.geofence_adv_edit.change_on_off(self.geofence_list[1], 0)
        else:
            self.geofence_adv_edit.change_on_off(self.geofence_list[1], 1)

        #3 OFF
        off = self.get_new_command(self.geofence_list[2], "status")
        # print(off)
        if off == 0:
            self.geofence_adv_edit.change_on_off(self.geofence_list[2], 1)
        else:
            self.geofence_adv_edit.change_on_off(self.geofence_list[2], 0)

        #4 visible
        visible = self.get_new_command(self.geofence_list[3], "visible")
        # print(visible)
        if visible == 1:
            self.geofence_adv_edit.change_visibility(self.geofence_list[3], 0)
        else:
            self.geofence_adv_edit.change_visibility(self.geofence_list[3], 1)

        #5 invisible
        invisible = self.get_new_command(self.geofence_list[4], "visible")
        # print(invisible)
        if invisible == 0:
            self.geofence_adv_edit.change_visibility(self.geofence_list[4], 1)
        else:
            self.geofence_adv_edit.change_visibility(self.geofence_list[4], 0)

        #6 coordinate
        points = self.get_new_command(self.geofence_list[5], "points")
        if points == self.points_1:
            print("---------------points_2")
            self.geofence_adv_edit.change_coordinate(self.geofence_list[5], self.points_2)
        else:
            print("---------------points_1")
            self.geofence_adv_edit.change_coordinate(self.geofence_list[5], self.points_1)

        #7 image
        self.swap_file_names()
        self.geofence_adv_edit.change_image(self.geofence_list[6], "Screenshot_1.png")
















