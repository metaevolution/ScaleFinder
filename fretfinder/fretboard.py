import pprint

from util import get_note_sequence
from util import scale_from_pattern
from util import SCALE_FORMULAS

TUNINGS = [
    {'name': 'E standard', 'notes' : ['E', 'A', 'D', 'G', 'B', 'E']}, 
    {'name': 'Drop D', 'notes' : ['D', 'A', 'D', 'G', 'B', 'E']}, 
    {'name': 'D standard', 'notes' : ['D', 'G', 'C', 'F', 'A', 'D']}, 
    {'name': 'Drop C', 'notes' : ['C', 'G', 'C', 'F', 'A', 'D']}, 
    {'name': 'Drop A', 'notes' : ['A', 'G', 'C', 'F', 'A', 'D']}
]

class String():

    def __init__(self, pitch):
        self.pitch = pitch

    def __repr__(self):
        return self.pitch


class Tuning():

    def __init__(self, name):
        self.strings = []
        self.name = name

    def add_string(self, string):
        self.strings.append(string)

    def __repr__(self):
        return "%s > %s" % (self.name, str(self.strings))


class Fret():

    def __init__(self, fret_num, width):
        self.fret_num = fret_num
        self.width = width

    def __repr__(self):
        return self.fret_num


class FretBoardASCIIRenderer():

    def __init__(self, fretboard, fret_width=6):
        self.row = "-"
        self.header_row = " "
        self.column = "|"
        self.nut = "|"
        self.corner = "+"
        self.header_corner = "|"
        self.fret_width = fret_width
        self.strings = len(fretboard.tuning.strings)
        self.frets = fretboard.frets
        self.rendered = ""
        self.fretboard = fretboard

    def _center(self, value, max_width, symbol):
        padding = ((max_width - len(str(value))) / 2)
        s = symbol * padding
        s += str(value)
        s += symbol * padding
        s += symbol * (max_width-len(s))
        return s

    def render(self):
        self.fretboard.generate() 
        output = ""
        output += "\r\n[Tuning: " + self.fretboard.tuning.name + "]\r"
        output += "\r\n[Scale: %s %s" % (self.fretboard.root_note, self.fretboard.scale_name)+ "]\r\n\r\n"

        header = self.header_corner
        for c in range(0, self.frets+1):
            if c == 1: # use a different symbol for nut.
                s = self.nut
            else:
                s = self.header_corner
            header += self._center(c, self.fret_width, self.header_row) + s

        output += header + "\r\n"
        for r in self.fretboard.fretboard: # TODO: Fix this awkward fretboard.fretboard reference.
            i = 0
            line = self.corner
            for c in r:
                if i == 0: # use a different symbol for nut.
                    s = self.nut
                else:
                    s = self.corner
                i+=1
                line += self._center(c, self.fret_width, self.row) + s
 
            output += line + "\r\n"
        print(output)
        


class FretBoard():

    def __init__(self, tuning, frets=24):
        self.frets = frets
        self.tuning = tuning
        self.fretboard = []
        self.scale_notes = None

    def set_scale(self, root_note, scale_name):
        self.scale_name = scale_name
        self.root_note = root_note
        self.scale_notes = scale_from_pattern(root_note, scale_name, SCALE_FORMULAS[scale_name])


    def generate(self):
        for s in self.tuning.strings:
            notes = get_note_sequence(s.pitch, self.frets, self.scale_notes)
            self.fretboard.append(notes)   
        return self.fretboard

    #def get_notes_on_string(self, string_index):
    #    """Return the note at string/fret coordinate."""
    #    print(get_note_sequence(self.tuning.strings[string_index].pitch, self.frets))

    def __repr__(self):
        return str(self.fretboard)



if __name__ == "__main__":
    
    import sys
    root_note = sys.argv[1]
    scale_name = sys.argv[2]
    tuning = sys.argv[3]

    for t in TUNINGS:
        if tuning == t['name']:
            t1 = Tuning(tuning)
            t['notes'].reverse() # reverse the strings list so that they appear on the fretboard in correct order
            for n in t['notes']:
                t1.add_string(String(n))
            break

    f1 = FretBoard(t1, 22)
    f1.set_scale(root_note, scale_name)


    #print(f1)
    #print(t1)
    #i = 0
    FretBoardASCIIRenderer(f1).render()

    #for s in f1.tuning.strings:
        #print("%s string >" % f1.tuning.strings[i].pitch)
        #print(f1.get_notes_on_string(i))
    #    i+=1
