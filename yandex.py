import requests
from config import TOKEN

API_BASE_URL = "https://cloud-api.yandex.net/"
disk_url = API_BASE_URL + "v1/disk"
folder_url = API_BASE_URL + "v1/disk/resources"

headers = {
    'accept': 'application/json',
    'authorization': f'OAuth {TOKEN}'
}


def get_disk_status(headers):
    return requests.get(disk_url, headers=headers).status_code


def folder_exist(folder_name, headers):
    return requests.get(folder_url, headers=headers, params={'path': folder_name}).status_code


def create_folder(folder_name, headers):
    if get_disk_status(headers) == 200:
        folder_url = API_BASE_URL + "v1/disk/resources"
        if folder_exist(folder_name, headers) == 404:
            requests.put(folder_url, headers=headers, params={'path': folder_name})
            if folder_exist(folder_name, headers) != 200:
                raise Exception('Папка не воздана, ошибка ввода!')
            print(f'Папка {folder_name} создана')
            return folder_exist(folder_name, headers)
        elif folder_exist(folder_name, headers) == 200:
            print(f'Папка {folder_name} уже существует')
            return folder_exist(folder_name, headers)
        else:
            return folder_exist(folder_name, headers)
    else:
        raise Exception('Отсутствует доступ к диску')


if __name__ == "__main__":
    folder_name = input('Введите название папки: ')
    print(create_folder(folder_name, headers))

