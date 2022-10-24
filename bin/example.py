from scalefinder.fretboard import FretBoard
from scalefinder.fretboard import Tuning
from scalefinder.fretboard import TUNINGS
from scalefinder.fretboard import FretBoardASCIIRenderer
from scalefinder.scales import Scale


if __name__ == "__main__":
    
    root_note = "C"
    scale_name = "C Major"
    scale_formula = "1 2 3 4 5 6 7" # Scale formulas are defined in scalefinder/const.py
    tuning = "(6-String Guitar) E standard" # Tunings are defined in scalefinder/fretboard.py

    t=[t for t in TUNINGS if tuning.lower() == t['name'].lower()][0]
    t1 = Tuning(tuning)
    t['notes'].reverse() # reverse the strings list so that they display on the fretboard in correct order
    [t1.add_string(n) for n in t['notes']]

    f1 = FretBoard(t1, 12)
    f1.set_scale(Scale(scale_name, root_note, scale_formula))
    print(FretBoardASCIIRenderer(f1).render())
