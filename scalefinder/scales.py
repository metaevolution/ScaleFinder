import pprint
from symtable import Symbol

from scalefinder.const import bcolors
from scalefinder.const import MAJOR_SCALE_FORMULA
from scalefinder.const import NOTES
from scalefinder.const import SCALE_FORMULAS
from scalefinder.const import SYMBOL_SHARP
from scalefinder.const import SYMBOL_FLAT
from scalefinder.const import SYMBOL_AUGMENTED
from scalefinder.const import SYMBOL_DIMINISHED


class Note():

    note = ""
    scale_degree = None
    is_root_note = False

    def __init__(self, note, scale_degree=None, is_root_note=False, pattern=None):
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
            if x.note == note:
                return x

    def get_notes_as_list(self):
        return [note.note for note in self.notes]

    def _scale_notes_filter(self, note):
        if (note.scale_degree):
            return True
        else:
            return False

    def get_scale_chords(self):
        #root_note = scale[0]['note']
        tmp_seq = note_sequence(self.root_note, 50, self)
        seq = list(filter(self._scale_notes_filter, tmp_seq)) # remove empty and leave only notes of scale
        chords = []
        for i in range(0,len(self.notes)):
            root = self.get_note(seq[i].note)
            third = self.get_note(seq[i+2].note)
            fifth = self.get_note(seq[i+4].note)
            chords.append([
                root, 
                third, 
                fifth
                ])
        return chords

    def __repr__(self) -> str:
        return f"Scale:{self.name} Notes:{self.notes} Chords:{self.chords}"


def note_sequence(starting_note, number_of_notes=50, scale=None):  # TODO: Move into a class
    notes = []
    note = Note(starting_note.upper(), 0)
    # get the root note
    if scale:
        a = [n for n in scale.notes if n.note == note.note]
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


def get_next_note(note): 
    """Return the next higher note in pitch"""
    position = NOTES.index(note.upper())
    if position == (len(NOTES) - 1):  # if at 11th position, start at position 0 (0 indexed)  
        position = 0
    else: 
        position += 1
    return NOTES[position]

def get_previous_note(note):
    """Return the next lower note in pitch"""
    position = NOTES.index(note.upper())
    if position == 0:  # if at 0 position, start at position 11 (0 indexed)  
        position = 11
    else: 
        position -= 1
    return NOTES[position]

def get_scale_candidates(submitted_notes, root_note=None, name_filter=None):
    """Find scales that contain all of the notes passed to function."""
    for scale_name, scale_formula in SCALE_FORMULAS.items():
        for rn in NOTES:
            scale = Scale(scale_name, rn, scale_formula)
            notes = scale.get_notes_as_list()
            if all(elem in notes for elem in submitted_notes):
                if root_note:
                    if rn == root_note:
                        yield {'scale': scale_name, 'formula': scale_formula, 'notes': notes, 'root_note': rn}
                else:
                    yield {'scale': scale_name, 'formula': scale_formula, 'notes': notes, 'root_note': rn}

if __name__ == "__main__":
    s = Scale("C Major","C","1 2 3 4b 5 6 7")
    for n in s.notes:
        print(n.note)
    print(s.get_note("C").note)
    print([x.note for x in note_sequence("C", 50, s)])
