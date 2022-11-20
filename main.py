import settings
import requests


def main():
    path_to_file = input('Введите полный путь к файлу: ')
    # path_to_file = '/Users/demolyky/Downloads/test.docx'
    uploader = YaUploader(settings.TOKEN)
    result = uploader.upload(path_to_file, detection_file_name(path_to_file))
    print(result)


def detection_file_name(file_path: str):
    return file_path.split(sep='/')[-1]


class YaUploader:

    HOST = 'https://cloud-api.yandex.net:443'

    def __init__(self, token):
        self.token = token

    def upload(self, file_path, ya_path):
        upload_url = self._get_link_url_upload(ya_path)
        responce = requests.put(upload_url, data=open(file_path, 'rb'), headers=self._get_headers())
        return responce

    def _get_link_url_upload(self, file_path):
        url = '/v1/disk/resources/upload/'
        requests_url = self.HOST + url
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(requests_url, headers=self._get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def _get_headers(self):
        return {
            'Content-Type': 'application.json',
            'Authorization': f'OAuth {self.token}'
            }


main()
