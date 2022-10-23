import unittest

from scalefinder.fretboard import FretBoardASCIIRenderer, Tuning, FretBoard
from scalefinder.scales import Note, note_sequence, Scale

class TestFretBoardRenderer(unittest.TestCase):

    #def test_calculate_major_scale_invalid(self): 
    #    with self.assertRaises(ValueError):
    #        calculate_major_scale("L#")

    def test_tuning(self):
        t1 = Tuning("E Standard")
        [t1.add_string(i) for i in ['E', 'A', 'D', 'G', 'B','E']]
        self.assertEqual(t1.strings, ['E', 'A', 'D', 'G', 'B', 'E']) 

    def test_tuning_name(self):
        t1 = Tuning("E Standard")
        [t1.add_string(i) for i in ['E', 'A', 'D', 'G', 'B','E']]
        self.assertEqual(t1.name, "E Standard") 

    def test_fretboard_render(self):
        t1 = Tuning("E Standard")
        [t1.add_string(i) for i in ['E', 'A']]
        f1 = FretBoard(t1,2)
        f1.set_scale(Scale("C Major", "C", "1 2 3 4 5 6 7"))
        result = FretBoardASCIIRenderer(f1).render()
        #self.assertEqual(result, "\x1b[92m\r\n[Tuning: E Standard] ['A'") 

if __name__ == '__main__':
    unittest.main()

