from fretfinder.fretboard import FretBoard
from fretfinder.fretboard import Tuning
from fretfinder.fretboard import TUNINGS
from fretfinder.fretboard import String
from fretfinder.fretboard import FretBoardASCIIRenderer


if __name__ == "__main__":
    
    import sys
    root_note = sys.argv[1]
    scale_name = sys.argv[2]
    tuning = sys.argv[3]

    for t in TUNINGS:
        if tuning == t['name']:
            t1 = Tuning(tuning)
            t['notes'].reverse() # reverse the strings list so that they display on the fretboard in correct order
            for n in t['notes']:
                t1.add_string(String(n))
            break

    f1 = FretBoard(t1, 22)
    f1.set_scale(root_note, scale_name)
    FretBoardASCIIRenderer(f1).render()
