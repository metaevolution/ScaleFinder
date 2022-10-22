# ScaleFinder
## Quickly find a scale on the guitar by providing a few starting notes.

# Requirments
Python 3.x or higher

# Setup 
`> git clone https://github.com/metaevolution/ScaleFinder.git
> cd ScaleFinder
> python3 setup.py install`

# Usage
`python3 bin/scale_finder.py  -h              
Usage: bin/scale_finder.py --notes A B C D F#
                

        -n, --notes:    Specify the notes you want to search relevant scales for. 
                        Separate multiple notes with spaces and surround with double quotes "". 
                        Use '#' for sharp, and 'b' for flat. e.g. 'Gb', 'A#' etc.
        -d, --degrees:  Show scale degrees instead of note names. 
        -i, --invert:   Shows notes that are NOT in the selected scale.
        -x, --xo_mode:  Show 'O' instead of note letters, or pair with -i to show 'X' for notes not in the scale.
        -v, --verbose:  Enable verbose output
        -h, --help:     This help menu
                `



