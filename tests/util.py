# these tests still need to be refactored 
""" import unittest

from scalefinder.util import get_previous_note
from scalefinder.util import get_next_note
from scalefinder.util import get_note_sequence
from scalefinder.util import get_relative_note
from scalefinder.util import calculate_major_scale

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
        self.assertEqual(result, ['(C)', '', '(D)', '(D#)', '(E)', '(F)', '(F#)', '', '(G#)', '', '(A#)', '(B)', '(C)'])

    def test_note_squence_w_length(self):
        result = get_note_sequence("C", 24, ['A'])
        self.assertEqual(result, ['', '', '', '', '', '', '', '', '', 'A', '', '', '', '', '', '', '', '', '', '', '', 'A', '', '',  ''])

    def test_note_degrees_wo_list(self): # This should ignore the scale degrees command.
        result = get_note_sequence("C", 12, None, False, True)
        self.assertEqual(result, ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C'])

    def test_note_degrees_w_list(self):
        result = get_note_sequence("C", 12, ['A','G#'], False, True)
        self.assertEqual(result, ['', '', '', '', '', '', '', '', 2, 1, '', '', ''])

    def test_note_xomode_wo_list(self): # This should ignore the scale degrees command.
        result = get_note_sequence("C", 12, None, False, False, True)
        self.assertEqual(result, ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C'])

    def test_note_xomode_w_list(self):
        result = get_note_sequence("C", 12, ['A','G#'], False, False, True)
        self.assertEqual(result, ['', '', '', '', '', '', '', '', 'O', 'O', '', '', ''])

class TestRelativeNote(unittest.TestCase):

    def test_relative_note(self):
        result = get_relative_note("B","b")
        self.assertEqual(result, "A#")

    def test_relative_note_lower(self):
        result = get_relative_note("b","b")
        self.assertEqual(result, "A#")

    def test_relative_note_upper_symbol(self):
        result = get_relative_note("b","B")
        self.assertEqual(result, "A#")

    def test_relative_note_end(self):
        result = get_relative_note("G","#")
        self.assertEqual(result, "A")

    def test_relative_note_end(self):
        result = get_relative_note("A","b")
        self.assertEqual(result, "G#")

class TestCalcMajorScale(unittest.TestCase):

    def test_calculate_major_scale(self):
        result = calculate_major_scale("B")
        self.assertEqual(result, ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'])    
        
    def test_calculate_major_scale_lower(self):
        result = calculate_major_scale("b")
        self.assertEqual(result, ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'])  

    def test_calculate_major_scale_end(self):
        result = calculate_major_scale("G#")
        self.assertEqual(result, ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'])    

    def test_calculate_major_scale_invalid(self): 
        with self.assertRaises(ValueError):
            calculate_major_scale("L#")

if __name__ == '__main__':
    unittest.main()
 """