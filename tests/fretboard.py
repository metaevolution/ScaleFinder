import unittest

from scalefinder.util import get_previous_note
from scalefinder.util import get_next_note
from scalefinder.util import get_note_sequence

class TestGetPreviousNote(unittest.TestCase):

    def test_get_previous_note_lower(self):
        result = get_previous_note("c#")
        self.assertEqual(result, "C")

    def test_get_previous_note_no_flats(self):
        with self.assertRaises(ValueError):
            get_previous_note("Cb")

    def test_get_previous_note_valid(self):
        result = get_previous_note("C")
        self.assertEqual(result, "B")

    def test_get_previous_note_A(self):
        result = get_previous_note("A")
        self.assertEqual(result, "G#")

    def test_get_previous_note_invalid(self):
        with self.assertRaises(ValueError):
            get_previous_note("K")


class TestGetNextNote(unittest.TestCase):

    def test_get_next_note_lower(self):
        result = get_next_note("c#")
        self.assertEqual(result, "D")

    def test_get_next_note_no_flats(self):
        with self.assertRaises(ValueError):
            get_next_note("Cb")

    def test_get_next_note_valid(self):
        result = get_next_note("C")
        self.assertEqual(result, "C#")

    def test_get_next_note_Gsharp(self):
        result = get_next_note("G#")
        self.assertEqual(result, "A")

    def test_get_next_note_invalid(self):
        with self.assertRaises(ValueError):
            get_next_note("K")

class TestNoteSequence(unittest.TestCase):

    def test_note_squence_no_list(self):
        result = get_note_sequence("C", 12)
        self.assertEqual(result, ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C'])

    def test_note_squence_lower(self):
        result = get_note_sequence("c", 12)
        self.assertEqual(result, ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C'])

    def test_note_squence_w_list(self):
        result = get_note_sequence("C", 12, ['A','C#','G'])
        self.assertEqual(result, ['', 'C#', '', '', '', '', '', 'G', '', 'A', '', '', ''])

    def test_note_squence_w_list_invalid(self):
        result = get_note_sequence("C", 12, ['L'])
        self.assertEqual(result, ['', '', '', '', '', '', '', '', '', '', '', '', ''])

    def test_note_squence_w_list_inverted(self):
        result = get_note_sequence("C", 12, ['A','C#','G'], inverted=True)
        self.assertEqual(result, ['C', '', 'D', 'D#', 'E', 'F', 'F#', '', 'G#', '', 'A#', 'B', 'C'])

if __name__ == '__main__':
    unittest.main()
