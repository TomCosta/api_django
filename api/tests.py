from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Note
from .serializers import NoteSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_note(id="", adat="", code="", name="", obs="", reba="", rena="", stat="", final="", created_at=""):
        if id != "" and adat != "":
            Note.objects.create(id=id, adat=adat, code=code, name=name, obs=obs, reba=reba, rena=rena, stat=stat,
                                final=final, created_at=created_at)

    def setUp(self):
        # add test data
        self.create_note(99905920, "2018-12-09", 7865, "Joelma e Chimbinha", "Musica Ruim do norte", 67321, "Maria Bernardes", 255, 1)
        self.create_note(99905943, "2018-12-12", 5423, "Chico Science Zumbi", "Musica Boa do norte", 21560, "Zeca Bernardes", 255, 0)
        self.create_note(99905910, "2018-12-30", 3215, "Dupla Sertaneja Sul", "Musica Central do Br", 67321, "Avanti e Frente", 255, 1)
        self.create_note(99905989, "2018-12-24", 7648, "Cristo Redentor Rio", "Musica Boa do mar", 67321, "Alice guimaraes", 255, 1)


class GetAllNoteTest(BaseViewTest):

    def test_get_all_note(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("note-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Note.objects.all()
        serialized = NoteSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)