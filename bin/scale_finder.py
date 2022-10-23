#!/usr/bin/env python3

import sys
import getopt

from scalefinder.scales import Scale
from scalefinder.scales import get_scale_candidates
from scalefinder.const import bcolors
from scalefinder.fretboard import FretBoard
from scalefinder.fretboard import Tuning
from scalefinder.fretboard import TUNINGS
from scalefinder.fretboard import FretBoardASCIIRenderer


if __name__ == "__main__":
    # defaults
    degrees = False
    verbose = False
    frets = 12
    fret_width = 6
    show_strings = True
    show_scale_degree = False
    minesweeper_mode = False
    filter_by_root_note = False
    filter_by_scale_name = False
    notes = ""

    argumentList = sys.argv[1:]
    
    # Options
    options = "vhn:dxr:sf:"
    
    # Long options
    long_options = ["notes=", "verbose", "help", "degrees", "xo_mode", "root_note=", "no_strings","filter=", "frets=", "fret_width=","minesweeper"]
    
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Help"):
                print(f"""Usage: {sys.argv[0]} --notes A B C D F#
                
        INPUTS:

        -n, --notes:        Specify the notes you want to search relevant scales for. 
                            Separate multiple notes with spaces and surround with double quotes \"\". 
                            Use '#' for sharp, and 'b' for flat. e.g. 'Gb', 'A#' etc.
        -r, --root_note:    Limit suggestions to scales with the provided root note.

        DISPLAY:

        -d, --degrees:      Show scale degrees instead of note names. 
        -x, --minesweeper:  Shows notes that are NOT in the selected scale.
        -f, --filter:       Filter by scales that contain user provided text (e.g. -f pentatonic).
        --frets:            (Default 12) Adjust the number of frets display. Useful for smaller screens.
        --fret_width:       (Default 6) Adjust the fretboard width. Useful for smaller screens.
        --no_strings:       Hide String letters to the left of the fretboard.

        MISC:

        -v, --verbose:      Enable verbose output
        -h, --help:         This help menu
                
                """)
                sys.exit(1)
                
            elif currentArgument in ("-n", "--notes"):
                notes = currentValue.split(" ")

            elif currentArgument in ("-r", "--root_note"):
                filter_by_root_note = currentValue

            elif currentArgument in ("-f", "--filter"): # TODO: WIP
                filter_by_scale_name = currentValue

            elif currentArgument in ("--frets"):
                frets = int(currentValue)

            elif currentArgument in ("--fret_width"):
                fret_width = int(currentValue)

            elif currentArgument in ("-v", "--verbose"):
                print(f"{bcolors.WARNING}[Option Enabled] verbose output mode{bcolors.ENDC}")
                verbose = True

            elif currentArgument in ("-d", "--degrees"):
                print(f"{bcolors.WARNING}[Option Enabled] scale degree output mode{bcolors.ENDC}")
                show_scale_degree = True
            
            elif currentArgument in ("-x", "--minesweeper"):
                print(f"{bcolors.WARNING}[Option Enabled] Minesweeper output mode{bcolors.ENDC}")
                minesweeper_mode = True

            elif currentArgument in ("--no_strings"):
                print(f"{bcolors.WARNING}[Option Enabled] Hide string names in fretboard output{bcolors.ENDC}")
                show_strings = False


    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))


    print(f"{bcolors.WARNING}\r\n[*] Found the following scales that include the notes %s:\r\n{bcolors.ENDC}" % (notes))
    n = 0 
    suggested_scales = []
    #for i in scale_candidate_iter(notes, filter_by_root_note):
    for i in get_scale_candidates(notes, filter_by_root_note):
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
        t1.add_string(n)

    f1 = FretBoard(t1, frets)
    f1.set_scale(Scale(scale['scale'], scale['root_note'], scale['formula']))
    print(FretBoardASCIIRenderer(f1, fret_width, 
            show_string_names=show_strings, 
            show_degree=show_scale_degree, 
            minesweeper_mode=minesweeper_mode
        ).render())
