from turtle import bgcolor
from scalefinder.const import bcolors
from scalefinder.const import SCALE_FORMULAS
from scalefinder.const import MAJOR_SCALE_FORMULA
from scalefinder.const import NOTES
from scalefinder.const import SYMBOL_SHARP
from scalefinder.const import SYMBOL_FLAT
from scalefinder.const import SYMBOL_AUGMENTED
from scalefinder.const import SYMBOL_DIMINISHED


def get_previous_note(note):
    """Return the next lower note in pitch"""

    position = NOTES.index(note.upper())
    if position == 0:  # if at 0 position, start at position 11 (0 indexed)  
        position = 11
    else: 
        position -= 1
    return NOTES[position]

def get_next_note(note):
    """Return the next higher note in pitch"""
    position = NOTES.index(note.upper())
    if position == (len(NOTES) - 1):  # if at 11th position, start at position 0 (0 indexed)  
        position = 0
    else: 
        position += 1
    return NOTES[position]

def _note_in_list(note, include_list, inverted=False, degrees=False, xo_mode=False):
    if not inverted:
        if note in include_list:
            if degrees:
                return include_list.index(note)+1
            elif xo_mode:
                return "O"
            else:
                return note
        else:
            return ""
    elif inverted:
        if note not in include_list:
            if xo_mode:
                return "X"
            else:
                return f"({note})"
        else:
            if xo_mode:
                return ""
            else:
                return ""   

def get_note_sequence(note, note_range, include_list=None, inverted=False, degrees=False, xo_mode=False):
    """Return the next x number of notes in sequential order. Use 'include_list' to return only notes within a scale."""
    notes = []
    note = note.upper()
    if include_list:
        notes.append(_note_in_list(note, include_list, inverted, degrees, xo_mode))
    else:
        notes.append(note)

    for i in range(1, note_range+1):
        note = get_next_note(note)
        if include_list:
            notes.append(_note_in_list(note, include_list, inverted, degrees, xo_mode))
        else:
            notes.append(note)
    return notes


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


def calculate_major_scale(root_note):
    """Returns the notes of the major scale for provided root note."""
    root_note = root_note.upper()
    FORMULA = [x for x in MAJOR_SCALE_FORMULA]
    note_len = len(NOTES)
    root_index = NOTES.index(root_note)
    scale = [root_note]
    position = root_index
    for f in FORMULA:
        if f == "W":
            if position == (len(NOTES) - 1):  # if at 11th position, start at position 1 (0 indexed)
                #print("%s: %s: %s: =1" % (f, position, NOTES[position]))
                position = 1
            elif position == (len(NOTES) - 2):  # if at 10th position, start at position 0 (0 indexed)
                #print("%s: %s: %s: =0" % (f, position, NOTES[position]))
                position = 0
            else: 
                #print("%s: %s: %s: +2" % (f, position, NOTES[position]))
                position += 2
        if f == "H":
            if position == (len(NOTES) - 1):  # if at 10th position, start at position 0 (0 indexed)
                #print("%s: %s: %s: =0" % (f, position, NOTES[position]))
                position = 0
            else:
                #print("%s: %s: %s: +1" % (f, position, NOTES[position]))
                position += 1
        scale.append(NOTES[position]) 
    scale.pop() # last note added is the root note again so pop it off the end of the list.
    return scale


def scale_from_pattern(root_note, scale_name, scale_pattern):
    """"""
    major = calculate_major_scale(root_note)
    pattern = scale_pattern.split(" ")
    scale = []
    for i in pattern:
        if len(i) == 1: # not sharp/flat
            note = major[int(i) - 1] 
        elif len(i) == 2: # sharp/flat/augmented, etc.
            note = get_relative_note(major[int(i[0]) - 1], i[1])
        scale.append(note)
    return(scale)



def generate_scales_iter(root_notes, scale_formulas):
    
    for k,v in scale_formulas.items():
        for j in root_notes:
            yield {'scale': k, 'formula': v, 'notes': scale_from_pattern(j, k, v), 'root_note': j}

        

def generate_scales(root_notes, scale_formulas):
    scales = []
    for k,v in scale_formulas.items():
        for j in root_notes:
            scales.append({'scale': k, 'formula': v, 'notes': scale_from_pattern(j, k, v), 'root_note': j})
    return scales


def scale_candidate_iter(submitted_notes, root_note=None):
    """Find scales that contain all of the notes passed to function."""
    for k,v in SCALE_FORMULAS.items():
        for j in NOTES:
            notes = scale_from_pattern(j, k, v)
            if all(elem in notes  for elem in submitted_notes):
                if root_note:
                    if j == root_note:
                        yield {'scale': k, 'formula': v, 'notes': notes, 'root_note': j}
                else:
                    yield {'scale': k, 'formula': v, 'notes': notes, 'root_note': j}

if __name__ == "__main__":
    import sys
    import pprint
    notes = sys.argv[1].split(" ")
    #root_note = sys.argv[1]
    #scale = sys.argv[2]

    #try:
    #    scale_formula = SCALE_FORMULAS[scale]
    #except KeyError:
    #    print("Scale %s not found." % scale)
    #    pprint.pprint(SCALE_FORMULAS)
    #    sys.exit(1)

    #print(scale_from_pattern(root_note, scale, scale_formula))
    print("[*] Found the following matches:")
    for i in scale_candidate_iter(notes):
        print("- %s %s \r\n  notes: %s\r\n" % (i['root_note'], i['scale'], i['notes']))
