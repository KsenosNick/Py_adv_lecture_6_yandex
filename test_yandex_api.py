import unittest
from yandex import create_folder, headers


class TestYandex(unittest.TestCase):

    def test_create_folder(self):
        self.folder_name = 'test_1'
        self.assertEqual(create_folder(self.folder_name, headers), 200)

    def test_create_folder_error(self):
        self.folder_name = 'test_2'
        with self.assertRaises(Exception):
            create_folder('test/3', headers)

    def test_auth_failed(self):
        self.folder_name = 'test_3'
        self.TOKEN = ''
        self.headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {self.TOKEN}'
        }
        with self.assertRaises(Exception):
            create_folder(self.folder_name, self.headers)


if __name__ == '__main__':
    unittest.main()
