from django.test import TestCase
from datetime import datetime
from unittest.mock import Mock
from common.utils import save_picture


class SavePictureTestCase(TestCase):
    def setUp(self):
        # Create a mock instance with a pk
        self.mock_instance = Mock()
        self.mock_instance._meta.app_label = 'your_app'
        self.mock_instance._meta.model_name = 'your_model'
        self.mock_instance.pk = 123

        self.filename = "example.jpg"
        raw_date = datetime.now()
        self.current_datetime = raw_date.strftime("%Y-%m-%d %H:%M:%S")

    def test_save_picture(self):
        expected_picture_name = (f"your_app/your_model/123/123_"
                                 f"{self.filename.split('.')[0]}"
                                 f"{self.current_datetime}."
                                 f"{self.filename.split('.')[-1]}")

        result = save_picture(self.mock_instance, self.filename)

        self.assertEqual(result, expected_picture_name)
