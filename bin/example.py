from scalefinder.fretboard import FretBoard
from scalefinder.fretboard import Tuning
from scalefinder.fretboard import TUNINGS
from scalefinder.fretboard import String
from scalefinder.fretboard import FretBoardASCIIRenderer


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
