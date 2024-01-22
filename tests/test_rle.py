import unittest
from archiving import RLE


def archive_unpack(text: str) -> str:
    archive = RLE.encode(text)
    unpack = RLE.decode(archive)
    return unpack


class TestArchiver(unittest.TestCase):

    def test_archive(self):
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

    def test_archiver_types(self):
        self.assertRaises(TypeError, RLE.encode, 5)
        self.assertRaises(TypeError, RLE.encode, 3.14)
        self.assertRaises(TypeError, RLE.encode, ['str'])
