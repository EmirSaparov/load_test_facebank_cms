from locust import HttpUser, task, tag


class Facebank(HttpUser):
    host = 'https://stage.facebank.store/api/v1/storage'

    @tag('orig1')
    @task
    def get_original_heavy(self):
        with open('uuids.txt', 'r') as file:
            lines = file.readlines()
            for uuid in lines:
                self.client.get(f'/original/{uuid.rstrip()}.jpg')

    @tag('orig2')
    @task
    def get_original_light(self):
        with open('uuids (2).txt', 'r') as file:
            lines = file.readlines()
            for uuid in lines:
                self.client.get(f'/original/{uuid.rstrip()}.jpg')

    @tag('thumb1')
    @task
    def get_thumbnail_heavy(self):
        with open('uuids.txt', 'r') as file:
            lines = file.readlines()
            for uuid in lines:
                self.client.get(f'/thumbnail/{uuid.rstrip()}.png')

    @tag('thumb2')
    @task
    def get_thumbnail_light(self):
        with open('uuids (2).txt', 'r') as file:
            lines = file.readlines()
            for uuid in lines:
                self.client.get(f'/thumbnail/{uuid.rstrip()}.png')

    @tag('prev1')
    @task
    def get_preview_heavy(self):
        with open('uuids.txt', 'r') as file:
            lines = file.readlines()
            for uuid in lines:
                self.client.get(f'/preview/{uuid.rstrip()}.png')

    @tag('prev2')
    @task
    def get_preview_light(self):
        with open('uuids (2).txt', 'r') as file:
            lines = file.readlines()
            for uuid in lines:
                self.client.get(f'/preview/{uuid.rstrip()}.png')
