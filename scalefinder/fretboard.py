from scalefinder.scales import Scale
from scalefinder.scales import note_sequence
from scalefinder.const import SCALE_FORMULAS
from scalefinder.const import bcolors

TUNINGS = [
    {'name': '(6-String Guitar) E standard', 'notes': ['E', 'A', 'D', 'G', 'B', 'E']}, 
    {'name': '(6-String Guitar) Drop D', 'notes': ['D', 'A', 'D', 'G', 'B', 'E']}, 
    {'name': '(6-String Guitar) D standard', 'notes': ['D', 'G', 'C', 'F', 'A', 'D']}, 
    {'name': '(6-String Guitar) Drop C', 'notes': ['C', 'G', 'C', 'F', 'A', 'D']}, 
    {'name': '(6-String Guitar) Drop B', 'notes': ['B', 'Gb', 'B', 'E', 'Ab', 'Db']}, 
    {'name': '(6-String Guitar) Drop A', 'notes': ['A', 'G', 'C', 'F', 'A', 'D']}, 
    {'name': '(6-String Guitar) Open D', 'notes': ['D', 'A', 'D', 'F#', 'A', 'D']},
    {'name': '(6-String Guitar) Open G', 'notes': ['D', 'G', 'D', 'G', 'B', 'D']},
    {'name': '(6-String Guitar) Open C', 'notes': ['C', 'G', 'C', 'G', 'C', 'E']},
    {'name': '(7-String Guitar) Standard', 'notes': ['B', 'E', 'A', 'D', 'G', 'B', 'E']},
    {'name': '(7-String Guitar) Drop A', 'notes': ['A', 'E', 'A', 'D', 'G', 'B', 'E']},
    {'name': '(4-String Bass) E standard', 'notes': ['E', 'A', 'D', 'G']}, 
    {'name': '(4-String Bass) Drop D', 'notes': ['D', 'A', 'D', 'G']}, 
    {'name': '(4-String Bass) D standard', 'notes': ['D', 'G', 'C', 'F']}, 
    {'name': '(4-String Bass) Drop C', 'notes': ['C', 'G', 'C', 'F']}, 
    {'name': '(4-String Bass) Drop B', 'notes': ['B', 'Gb', 'B', 'E']}, 
    {'name': '(4-String Bass) Drop A', 'notes': ['A', 'G', 'C', 'F']}, 
    {'name': '(5-String Bass) E standard', 'notes': ['E', 'A', 'D', 'G', 'B']}, 
    {'name': '(5-String Bass) Drop D', 'notes': ['D', 'A', 'D', 'G', 'B']}, 
    {'name': '(5-String Bass) D standard', 'notes': ['D', 'G', 'C', 'F', 'A']}, 
    {'name': '(5-String Bass) Drop C', 'notes': ['C', 'G', 'C', 'F', 'A']}, 
    {'name': '(5-String Bass) Drop B', 'notes': ['B', 'Gb', 'B', 'E', 'Ab']}, 
    {'name': '(5-String Bass) Drop A', 'notes': ['A', 'G', 'C', 'F', 'A']}, 
]


class Tuning():

    def __init__(self, name):
        self.strings = []
        self.name = name

    def add_string(self, string):
        self.strings.append(string)

    def __repr__(self):
        return "%s > %s" % (self.name, str(self.strings))


class FretBoardASCIIRenderer():

    def __init__(self, fretboard, fret_width=6, show_tuning=True, 
                show_degree=False, show_inverted=False, minesweeper_mode=False):
        self.row = "-"
        self.header_row = " "
        self.column = "|"
        self.nut = "|"
        self.corner = "+"
        self.header_corner = "|"
        self.show_tune = show_tuning
        self.show_inverted = show_inverted
        self.show_degree = show_degree
        self.minesweeper_mode = minesweeper_mode
        self.fret_width = fret_width
        self.strings = len(fretboard.tuning.strings)
        self.frets = fretboard.frets
        self.rendered = ""
        self.fretboard = fretboard

    def _center(self, value, max_width, symbol):
        """Center ASCII Text"""
        padding = ((max_width - len(str(value))) / 2)
        s1 = symbol * int(padding)
        s1 += str(value)
        s1 += symbol * int(padding)
        s1 += symbol * (max_width-len(s1))   
        return s1

    def render(self):
        """Create an ASCII representation of a fretboard."""
        output = ""
        output += f"{bcolors.OKGREEN}\r\n[Tuning: {self.fretboard.tuning.name}] {str(self.fretboard.tuning.strings[::-1])}\r{bcolors.ENDC}"
        output += f"{bcolors.OKCYAN}\r\nScale: [{self.fretboard.scale.root_note} {self.fretboard.scale.name}] \r\nFormula: [{self.fretboard.scale.formula}] \r\nNotes: {[x.note for x in self.fretboard.scale.notes]}\r\n\r\n{bcolors.ENDC}"
        if not self.show_tune:
            header = "|"
        else:
            header = self._center("Str" , self.fret_width, " ") + "|"
        for c in range(0, self.frets+1):
            if c == 1: # use a different symbol for nut.
                s = self.nut
            else:
                s = self.header_corner
            header += self._center(c, self.fret_width, self.header_row) + s

        output += header + "\r\n"
        n = 0
        for r in self.fretboard.fretboard: # TODO: Fix this awkward fretboard.fretboard reference.
            i = 0
            if not self.show_tune:
                line = "|"
            else:
                line = self._center(f"-{self.fretboard.tuning.strings[n]}-", self.fret_width, " ") + "|"
            n += 1
            for c in r:
                if i == 0: # use a different symbol for nut.
                    s = self.nut
                else:
                    s = self.corner
                i += 1
                if self.show_degree:
                    a = c.scale_degree
                else:
                    a = c.note
                if a:
                    b = a
                else:
                    b = ""
                line += self._center(b, self.fret_width, self.row) + s

            output += line + "\r\n"
        n = 1
        output += "\r\n"
        output += "[Scale Chords]\r\n"
        output += "   Triad Notes:   Scale Degrees:\r\n"
        for i in self.fretboard.scale.get_scale_chords():
            output += f"{n} {[x.note for x in i]} {[x.scale_degree for x in i]}\r\n"
            n += 1
        return output
        

class FretBoard():
    """Data model for a fretboard."""
    def __init__(self, tuning, frets=24):
        self.frets = frets
        self.tuning = tuning
        self.fretboard = []
        self.scale = None

        #self.show_inverted = inverted
        #self.show_scale_degrees = degrees
        #self.xo_mode = xo_mode

    def set_scale(self, scale):
        self.fretboard = []
        self.scale = scale
        for string in self.tuning.strings:
            notes = note_sequence(string, self.frets, self.scale)
            self.fretboard.append(notes)  


    def __repr__(self):
        return str(self.fretboard)


if __name__ == "__main__":
    
    import sys
    t = TUNINGS[0]
    t1 = Tuning(t['name'])
    t['notes'].reverse() # reverse the strings list so that they display on the fretboard in correct order
    for n in t['notes']:
        t1.add_string(n)

    f1 = FretBoard(t1, 12)
    f1.set_scale(Scale("C Major", "C", "1 2 3 4 5 6 7"))
    print(FretBoardASCIIRenderer(f1).render())
