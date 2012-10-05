from django.utils.unittest import TestCase
from django.forms import CharField

from apps import forms


class SetEnvFormTest(TestCase):
    def test_forms_should_contains_SetEnvForm(self):
        self.assertTrue(hasattr(forms, 'SetEnvForm'))

    def test_should_have_app_field(self):
        self.assertIn('app', forms.SetEnvForm.base_fields)

    def test_app_field_should_have_CharField(self):
        field = forms.SetEnvForm.base_fields['app']
        self.assertTrue(isinstance(field, CharField))

    def test_app_field_should_have_at_most_60_characters(self):
        field = forms.SetEnvForm.base_fields['app']
        self.assertEqual(60, field.max_length)

    def test_should_have_env_field(self):
        self.assertIn('env', forms.SetEnvForm.base_fields)

    def test_env_field_should_have_CharField(self):
        field = forms.SetEnvForm.base_fields['env']
        self.assertTrue(isinstance(field, CharField))

    def test_env_field_should_have_at_most_1000_characters(self):
        field = forms.SetEnvForm.base_fields['env']
        self.assertEqual(1000, field.max_length)