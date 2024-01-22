import unittest
from archiving import BWT


def archive_unpack(text: str) -> str:
    archive, position = BWT.encode(text)
    unpack = BWT.decode(archive, position)
    return unpack


class TestBWT(unittest.TestCase):

    def test_encode(self):
        text: str = 'AAABBBCCDDE'
        self.assertEqual(archive_unpack(text), text)
        text = 'A5755//BED'
        self.assertEqual(archive_unpack(text), text)
        text = 'askdhjfASDFJASDASSSASE'
        self.assertEqual(archive_unpack(text), text)
        text = '\\n\\'
        self.assertEqual(archive_unpack(text), text)
        text = 'ba7n7ana7'
        self.assertEqual(archive_unpack(text), text)
        text = '777751'
        self.assertEqual(archive_unpack(text), text)

    def test_bwt_encode_types(self):
        self.assertRaises(TypeError, BWT.encode, 5)
        self.assertRaises(TypeError, BWT.encode, 3.14)
        self.assertRaises(TypeError, BWT.encode, ['str'])

    def test_bwt_decode_types(self):
        self.assertRaises(TypeError, BWT.decode, 5, 1)
        self.assertRaises(TypeError, BWT.decode, 3.14, 1)
        self.assertRaises(TypeError, BWT.decode, ['str'], 1)

        self.assertRaises(TypeError, BWT.decode, 'str', 'str')
        self.assertRaises(TypeError, BWT.decode, 'str', 1.1)
        self.assertRaises(TypeError, BWT.decode, 'str', 5j)

    def test_archiver_values(self):
        self.assertRaises(ValueError, BWT.decode, 'str', -1)
        self.assertRaises(ValueError, BWT.decode, 'str', -2)
        self.assertRaises(ValueError, BWT.decode, 'str', -436)
