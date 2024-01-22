import unittest
from archive import Archiver


def archive_unpack(text: str) -> str:
    archive = Archiver.archiver(text)
    unpack = Archiver.unpacker(archive)
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

    def test_archive_without_bwt(self):
        text: str = 'AAABBBCCDDE'
        self.assertEqual(archive_unpack(text), text, False)
        text = 'A5755//BED'
        self.assertEqual(archive_unpack(text), text, False)
        text = 'askdhjfASDFJASDASSSASE'
        self.assertEqual(archive_unpack(text), text, False)
        text = '\\n\\'
        self.assertEqual(archive_unpack(text), text, False)
        text = 'ba7n7ana7'
        self.assertEqual(archive_unpack(text), text, False)
        text = '777751'
        self.assertEqual(archive_unpack(text), text)

    def test_archiver_types(self):
        self.assertRaises(TypeError, Archiver.archiver, 5)
        self.assertRaises(TypeError, Archiver.archiver, 3.14)
        self.assertRaises(TypeError, Archiver.archiver, ['str'])

    def test_unpacker_types(self):
        self.assertRaises(TypeError, Archiver.unpacker, 5)
        self.assertRaises(TypeError, Archiver.unpacker, 3.14)
        self.assertRaises(TypeError, Archiver.unpacker, ['str'])
