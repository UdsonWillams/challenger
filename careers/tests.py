# Create your tests here.

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from careers.models import Careers


class ListCreateCareersViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.get_or_create = "/careers/"
        self.career_data = {
            "username": "fernando-senna",
            "title": "Develops software solutions.",
            "content": "Develops software solutions for clients who know what they want.",
        }

    def test_create_career(self):
        response = self.client.post(self.get_or_create, self.career_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Careers.objects.count(), 1)
        self.assertEqual(Careers.objects.get().username, "fernando-senna")

    def test_list_careers(self):
        Careers.objects.create(
            username="fernando-senna", content="Develops software solutions."
        )
        response = self.client.get(self.get_or_create, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), 1)
        self.assertEqual(response.data["results"][0]["username"], "fernando-senna")


class PatchOrDeleteCareersViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.career = Careers.objects.create(
            username="Software Engineer",
            title="Develops software solutions.",
            content="Develops software solutions for clients who know what they want.",
        )
        self.url_patch_or_delete = f"/careers/{self.career.id}"
        self.patch_data = {"content": "Develops and maintains software solutions."}

    def test_patch_career(self):
        response = self.client.patch(
            self.url_patch_or_delete, self.patch_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.career.refresh_from_db()
        self.assertEqual(
            self.career.content, "Develops and maintains software solutions."
        )

    def test_delete_career(self):
        response = self.client.delete(self.url_patch_or_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Careers.objects.count(), 0)
