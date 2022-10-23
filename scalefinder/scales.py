import pprint
from symtable import Symbol

from scalefinder.const import bcolors
from scalefinder.const import SCALE_FORMULAS
from scalefinder.const import MAJOR_SCALE_FORMULA
from scalefinder.const import NOTES
from scalefinder.const import SYMBOL_SHARP
from scalefinder.const import SYMBOL_FLAT
from scalefinder.const import SYMBOL_AUGMENTED
from scalefinder.const import SYMBOL_DIMINISHED


def calculate_major_scale(root_note):
    """Returns the notes of the major scale for provided root note."""
    root_note = root_note.upper()
    root_index = NOTES.index(root_note)
    cursor = root_index
    scale = [root_note]
    for f in [x for x in MAJOR_SCALE_FORMULA]:
        if f == "W":
            if cursor == (len(NOTES) - 1):  # if at 11th position, start at position 1 (0 indexed)
                cursor = 1
            elif cursor == (len(NOTES) - 2):  # if at 10th position, start at position 0 (0 indexed)
                cursor = 0
            else: 
                cursor += 2
        if f == "H":
            if cursor == (len(NOTES) - 1):  # if at 10th position, start at position 0 (0 indexed)
                cursor = 0
            else:
                cursor += 1
        scale.append(NOTES[cursor])
    scale.pop() # last note added is the root note again so pop it off the end of the list.
    return scale

def get_relative_note(note, symbol):
    """Return the note sharp or flat of the provided note"""
    note = note.upper()
    symbol = symbol.lower()
    position = NOTES.index(note)
    if symbol == SYMBOL_SHARP or symbol == SYMBOL_AUGMENTED:
        if position == (len(NOTES) - 1):  # if at 11th position, start at position 0 (0 indexed)  
            position = 0
        else: 
            position += 1
    elif (symbol == SYMBOL_FLAT or symbol == SYMBOL_DIMINISHED):
        if position == 0:  # if at 0 position, start at position 11 (0 indexed)  
            position = 11
        else: 
            position -= 1
    return NOTES[position]


def get_scale_triads(scale):
    """"""
    root_note = scale[0]['note']
    seq = get_note_sequence(root_note, 50, scale)
    seq = list(filter(None, seq)) # remove empty and leave only notes of scale
    pprint.pprint(scale)
    chords = []
    for i in range(0,7):
        root = i
        third = i+2
        fifth = third+2
        chords.append({'notes': [seq[root], seq[third], seq[fifth]], 
                    'degrees': [root+1, third+1, fifth+1]})
    return chords

def _note_in_scale(note, scale, inverted=False, degrees=False, xo_mode=False): # TODO: Refactor this method
    if not inverted:
        #print([d for d in scale if d["note"] == note])
        #print(a)
        if 1==2:
            if degrees:
                return scale.index(note)+1
            elif xo_mode:
                return "O"
            else:
                return note
        else:
            return ""
    elif inverted:
        if note not in scale:
            if xo_mode:
                return "X"
            else:
                return f"({note})"
        else:
            if xo_mode:
                return ""
            else:
                return ""   


def get_next_note(note):
    """Return the next higher note in pitch"""
    position = NOTES.index(note.upper())
    if position == (len(NOTES) - 1):  # if at 11th position, start at position 0 (0 indexed)  
        position = 0
    else: 
        position += 1
    return NOTES[position]

def get_note_sequence(note, note_range, scale=None, inverted=False, degrees=False, xo_mode=False): 
    """Return the next x number of notes in sequential order. Use 'include_list' to return only notes within a scale."""
    notes = []
    note = note.upper()
    # get the root note
    if scale:
        a = [d for d in scale if d["note"] == note]
        if len(a) == 1:
            notes.append(a[0])
        else:
            notes.append({"degree": "", "note": ""})
    else:
        notes.append(note)

    # calculate the next notes in sequence
    for i in range(1, note_range+1):
        note = get_next_note(note)
        if scale:
            a = [d for d in scale if d["note"] == note]
            if len(a) == 1:
                notes.append(a[0])
            else:
                notes.append({"degree": "", "note": ""})
        else:
            notes.append(note)
    return notes

def construct_scale(root_note, scale_pattern):
    """Construct a scale from it's root note and the scale degrees.
    Example: \"1 2 3 4 5 6 7b\""""
    major = calculate_major_scale(root_note)
    pattern = scale_pattern.split(" ")
    scale = []
    for i in pattern:
        if len(i) == 1: # not sharp/flat
            note = major[int(i) - 1] 
        elif len(i) == 2: # sharp/flat/augmented, etc.
            cursor = int(i[0]) - 1
            symbol = i[1]
            note = get_relative_note(major[cursor], symbol)
        scale.append({'note': note, 'degree': int(i[0])})
    return(scale)

class Note():

    note = ""
    scale_degree = None
    is_root_note = False

    def __init__(self, note, scale_degree=0, is_root_note=False, pattern=None):
        self.note = note
        self.scale_degree = scale_degree
        self.is_root_note = is_root_note
        self.pattern = pattern

    #def __repr__(self) -> str:
    #    return f"[Note: {self.note} Root?:{self.is_root_note} Degree:{self.scale_degree} Pattern:{self.pattern}]"


class Scale():

    def __init__(self, name, root_note, formula):
        self.name = name
        self.root_note = root_note
        self.formula = formula
        self.chords = []
        self.notes = []
        self._construct_scale()
        self.__index = 0

    def _construct_scale(self):
        """Construct a scale from it's root note and the scale degrees.
        Example: \"1 2 3 4 5 6 7b\""""
        major = self._calculate_major_scale()
        pattern = self.formula.split(" ")
        first = True # flag the first note added as the root note
        for i in pattern:
            if len(i) == 1: # not sharp/flat
                note = major[int(i) - 1] 
            elif len(i) == 2: # sharp/flat/augmented, etc.
                cursor = int(i[0]) - 1
                symbol = i[1]
                note = self._get_relative_note(major[cursor], symbol)
            
            self.notes.append(Note(note, int(i[0]), first, i))
            first = False

    def _calculate_major_scale(self):
        """Returns the notes of the major scale for provided root note."""
        root_note = self.root_note.upper()
        root_index = NOTES.index(root_note)
        cursor = root_index
        scale = [root_note]
        for f in [x for x in MAJOR_SCALE_FORMULA]:
            if f == "W":
                if cursor == (len(NOTES) - 1):  # if at 11th position, start at position 1 (0 indexed)
                    cursor = 1
                elif cursor == (len(NOTES) - 2):  # if at 10th position, start at position 0 (0 indexed)
                    cursor = 0
                else: 
                    cursor += 2
            if f == "H":
                if cursor == (len(NOTES) - 1):  # if at 10th position, start at position 0 (0 indexed)
                    cursor = 0
                else:
                    cursor += 1
            scale.append(NOTES[cursor])
        scale.pop() # last note added is the root note again so pop it off the end of the list.
        return scale

    def _get_relative_note(self, note, symbol):
        """Return the note sharp or flat of the provided note"""
        note = note.upper()
        symbol = symbol.lower()
        position = NOTES.index(note)
        if symbol == SYMBOL_SHARP or symbol == SYMBOL_AUGMENTED:
            if position == (len(NOTES) - 1):  # if at 11th position, start at position 0 (0 indexed)  
                position = 0
            else: 
                position += 1
        elif (symbol == SYMBOL_FLAT or symbol == SYMBOL_DIMINISHED):
            if position == 0:  # if at 0 position, start at position 11 (0 indexed)  
                position = 11
            else: 
                position -= 1
        return NOTES[position]

    def get_note(self, note):
        #a = [x for x in self.notes if x.note == note.note]
        for x in self.notes:
            if x.note == note.note:
                return x


    def _scale_notes(self, note):
        if (note.scale_degree > 0):
            return True
        else:
            return False

    def get_scale_chords(self):
        #root_note = scale[0]['note']
        tmp_seq = note_sequence(self.root_note, 50, self)
        seq = list(filter(self._scale_notes, tmp_seq)) # remove empty and leave only notes of scale
        chords = []
        for i in range(0,7):
            root = self.get_note(seq[i])
            third = self.get_note(seq[i+2])
            fifth = self.get_note(seq[i+4])
            chords.append([
                root, 
                third, 
                fifth
                ])
        return chords

    def __repr__(self) -> str:
        return f"Scale:{self.name} Notes:{self.notes} Chords:{self.chords}"


def note_sequence(starting_note, number_of_notes=50, scale=None): 
        notes = []
        note = Note(starting_note.upper(), 0)
        # get the root note
        if scale:
            a = [n for n in scale.notes if n.note == note.note]

            print(a)
            if len(a) == 1:
                notes.append(a[0])
            else:
                notes.append(Note(""))
        else:
            notes.append(note)

        # calculate the next notes in sequence
        for i in range(1, number_of_notes+1):
            note = Note(get_next_note(note.note), 0)
            if scale:
                a = [n for n in scale.notes if n.note == note.note]
                if len(a) == 1:
                    notes.append(a[0])
                else:
                    notes.append(Note(""))
            else:
                notes.append(note)
        return notes

if __name__ == "__main__":
    #pprint.pprint(calculate_major_scale("C"))
    s = Scale("C Major","C","1 2 3 4b 5 6 7")
    #for n in s.notes:
    #    print(n)
    #for n in s.notes:
    #    print(n)
    #print(s.get_note("C"))
    #print(note_sequence("C", 50, s))
    print(s)