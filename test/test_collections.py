import unittest

from pydantic.error_wrappers import ValidationError

from cgwain.collection import Collection

class TestBaseCollections(unittest.TestCase):
    def test_required_fields(self):
        """Fields that are required should raise an exception and be of the correct type"""
        with self.assertRaises(ValidationError):
            Collection()
        with self.assertRaises(ValidationError):
            Collection(name='foo')

    def test_empty_fields(self):
        """Empty fields that have a specified default should omit them"""
        bare_minimum = Collection(name='foo', fields=[])
        target_dict = {
            'name': 'foo',
            'fields': []
        }
        self.assertDictEqual(bare_minimum.dict(), target_dict)