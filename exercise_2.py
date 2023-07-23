import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        name_path = path_to_file.split('\\')
        file_path = name_path[-1]
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": "/" + file_path}
        headers = {'Authorization': "OAuth " + token}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        url = data['href']
        with open(path_to_file, 'rb') as f:
            requests.put(url, files={'file': f})
        print(response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:\\Users\\anast\\Desktop\\000000843.jpg"
    token = open("token").read()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
