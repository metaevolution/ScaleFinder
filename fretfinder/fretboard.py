import pprint

from util import get_note_sequence

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

    def __init__(self, frets=24, strings=6, fret_width=6):
        self.row = "-"
        self.header_row = " "
        self.column = "|"
        self.corner = "+"
        self.header_corner = "|"
        self.fret_width = fret_width
        self.strings = strings
        self.frets = frets
        self.rendered = ""

    def _center(self, value, max_width, symbol):
        padding = ((max_width - len(str(value))) / 2)
        s = symbol * padding
        s += str(value)
        s += symbol * padding
        s += symbol * (max_width-len(s))
        return s

    def render(self, fretboard):
        
        header = self.header_corner
        for c in range(0, self.frets+1):
            header += self._center(c, self.fret_width, self.header_row) + self.header_corner

        print(header)
        for r in fretboard:
            line = self.corner
            for c in r:
                line += self._center(c, self.fret_width, self.row) + self.corner

            print(line)
        

    def __repr__(self):
        return str(self.fretboard) 


class FretBoard():

    def __init__(self, tuning, frets=24):
        self.frets = frets
        self.tuning = tuning
        self.fretboard = []

    def generate(self):
        for s in self.tuning.strings:
            notes = get_note_sequence(s.pitch, self.frets)
            self.fretboard.append(notes)   
        return self.fretboard

    def get_notes_on_string(self, string_index):
        """Return the note at string/fret coordinate."""
        print(get_note_sequence(self.tuning.strings[string_index].pitch, self.frets))

    def __repr__(self):
        return str(self.fretboard)



if __name__ == "__main__":
    
    t1 = Tuning("E Standard")
    f1 = FretBoard(t1)
    t1.add_string(String("E"))
    t1.add_string(String("A"))
    t1.add_string(String("D"))
    t1.add_string(String("G"))
    t1.add_string(String("B"))
    t1.add_string(String("E"))
    #print(f1)
    #print(t1)
    #i = 0
    fretboard = f1.generate()
    print(f1)
    FretBoardASCIIRenderer().render(fretboard)

    #for s in f1.tuning.strings:
        #print("%s string >" % f1.tuning.strings[i].pitch)
        #print(f1.get_notes_on_string(i))
    #    i+=1
