#!/usr/bin/env python3

import sys
import getopt

from scalefinder.util import scale_candidate_iter
from scalefinder.const import bcolors
from scalefinder.fretboard import FretBoard
from scalefinder.fretboard import Tuning
from scalefinder.fretboard import TUNINGS
from scalefinder.fretboard import String
from scalefinder.fretboard import FretBoardASCIIRenderer

if __name__ == "__main__":
    # defaults
    inverted = False
    degrees = False
    verbose = False
    xo_mode = False
    notes = ""

    argumentList = sys.argv[1:]
    
    # Options
    options = "vhin:dx"
    
    # Long options
    long_options = ["notes=", "invert", "verbose", "help", "degrees", "xo_mode"]
    
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Help"):
                print(f"""Usage: {sys.argv[0]} --notes A B C D F#
                

        -n, --notes:    Specify the notes you want to search relevant scales for. 
                        Separate multiple notes with spaces and surround with double quotes \"\". 
                        Use '#' for sharp, and 'b' for flat. e.g. 'Gb', 'A#' etc.
        -d, --degrees:  Show scale degrees instead of note names. 
        -i, --invert:   Shows notes that are NOT in the selected scale.
        -x, --xo_mode:  Show 'O' instead of note letters, or pair with -i to show 'X' for notes not in the scale.
        -v, --verbose:  Enable verbose output
        -h, --help:     This help menu
                
                """)
                sys.exit(1)
                
            elif currentArgument in ("-n", "--notes"):
                notes = currentValue.split(" ")
                
            elif currentArgument in ("-i", "--invert", ):
                print(("Enabling inverted output mode (% s)") % (currentValue))
                inverted = True

            elif currentArgument in ("-v", "--verbose"):
                print(("Enabling verbose output mode (% s)") % (currentValue))
                verbose = True

            elif currentArgument in ("-d", "--degrees"):
                print(("Enabling scale degree output mode (% s)") % (currentValue))
                degrees = True
            
            elif currentArgument in ("-x", "--xo_mode"):
                print(("Enabling XO output mode (% s)") % (currentValue))
                xo_mode = True
                
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))


    print(f"{bcolors.WARNING}\r\n[*] Found the following scales that include the notes %s:\r\n{bcolors.ENDC}" % (notes))
    n = 0 
    suggested_scales = []
    for i in scale_candidate_iter(notes):
        suggested_scales.append(i)
        #print("%s. %s %s" % (n, i['root_note'], i['scale']))
        if verbose:
            print("%s. %s %s notes: %s formula: %s" % (n, i['root_note'], i['scale'], i['notes'], i['formula']))
        else:
            print("%s. %s %s" % (n, i['root_note'], i['scale']))
        n+=1

    if len(suggested_scales) == 0:
        print("[*] No scales found with notes: %s" % notes)
        sys.exit(0)
    else:
        print(f"{bcolors.HEADER}\r\n[*] Found scales that include the notes %s:\r\n{bcolors.ENDC}" % (notes))
        variable = input(f"{bcolors.WARNING}[*] Please enter the corresponding number for the scale you want to see on the fretboard, or 'n' to exit: {bcolors.ENDC}")
        if variable == 'n':
            sys.exit(0)
        scale = suggested_scales[int(variable)] 

    n = 0 
    print("")
    for t in TUNINGS:
        print("%s. %s" % (n, t['name']))
        n += 1
    
    variable = input(f"{bcolors.WARNING}'\r\n[*] Please select the tuning to use:  {bcolors.ENDC}")
        
    t = TUNINGS[int(variable)]
    t1 = Tuning(t['name'])
    t['notes'].reverse() # reverse the strings list so that they display on the fretboard in correct order
    for n in t['notes']:
        t1.add_string(String(n))

    f1 = FretBoard(t1, 24, inverted, degrees, xo_mode)
    f1.set_scale(scale['root_note'], scale['scale'])
    FretBoardASCIIRenderer(f1).render()
