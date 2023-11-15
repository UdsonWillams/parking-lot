from locust import (
    HttpUser,
    task,
)


class TestLocust(HttpUser):
    """
    a classe de teste de carga
    """

    @task
    def get_user(self):
        """
        testando endpoint
        """
        endpoint = ""
        headers = {
            "x-client-id": "123",
            "x-user-id": "abc-123-4frg",
            "accept-language": "pt-BR",
        }
        self.client.get(endpoint, headers=headers)
