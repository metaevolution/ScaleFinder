#!/usr/bin/env python3

import sys
import getopt

from fretfinder.util import scale_candidate_iter
from fretfinder.fretboard import FretBoard
from fretfinder.fretboard import Tuning
from fretfinder.fretboard import TUNINGS
from fretfinder.fretboard import String
from fretfinder.fretboard import FretBoardASCIIRenderer

if __name__ == "__main__":
    inverted = False
    notes = ""

    argumentList = sys.argv[1:]
    
    # Options
    options = "h"
    
    # Long options
    long_options = ["notes=", "invert", "help"]
    
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Help"):
                print("Usage: %s --notes \"A B C D F#\"")
                
            elif currentArgument in ("-n", "--notes"):
                notes = currentValue.split(" ")
                
            elif currentArgument in ("-i", "--invert"):
                print(("Enabling inveted output mode (% s)") % (currentValue))
                inverted = True
                
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))


    print("\r\n[*] Found the following scales that include the notes %s:\r\n" % (notes))
    n = 0 
    suggested_scales = []
    for i in scale_candidate_iter(notes):
        suggested_scales.append(i)
        print("%s. %s %s \r\n  notes: %s\r\n" % (n, i['root_note'], i['scale'], i['notes']))
        n+=1

    if len(suggested_scales) == 0:
        print("[*] No scales found with notes: %s" % notes)
        sys.exit(0)
    else:
        print("[*] %s scales found with notes: %s" % (len(suggested_scales),notes))
        variable = input('[*] Please enter the number of the scale you want to see on the fretboard: ')
        scale = suggested_scales[int(variable)] 

    n = 0 
    print("")
    for t in TUNINGS:
        print("%s. %s" % (n, t['name']))
        n += 1
    
    variable = input('[*] Please select the tuning to use: ')
        
    t = TUNINGS[int(variable)]
    t1 = Tuning(t['name'])
    t['notes'].reverse() # reverse the strings list so that they display on the fretboard in correct order
    for n in t['notes']:
        t1.add_string(String(n))

    f1 = FretBoard(t1, 24, inverted)
    f1.set_scale(scale['root_note'], scale['scale'])
    FretBoardASCIIRenderer(f1).render()
