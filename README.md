# ScaleFinder
## Quickly find a scale on the guitar by providing a few starting notes.

# Usage
```      
    Usage: scale_finder --notes A B C D F#
                
        INPUTS:

        -n, --notes:        Specify the notes you want to search relevant scales for. 
                            Separate multiple notes with spaces and surround with double quotes "". 
                            Use '#' for sharp, and 'b' for flat. e.g. 'Gb', 'A#' etc.
        -r, --root_note:    Limit suggestions to scales with the provided root note.

        DISPLAY:

        -d, --degrees:      Show scale degrees instead of note names. 
        -x, --minesweeper:  Shows notes that are NOT in the selected scale.
        --frets:            (Default 12) Adjust the number of frets display. Useful for smaller screens.
        --fret_width:       (Default 6) Adjust the fretboard width. Useful for smaller screens.
        --no_strings:       Hide String letters to the left of the fretboard.

        MISC:

        -v, --verbose:      Enable verbose output
        -h, --help:         This help menu
                

```

# Example Output
```
> scale_finder -n "C E G A F#"  

[*] Found the following scales that include the notes ['C', 'E', 'G', 'A', 'F#']:

0. C lydian
1. G major
2. D mixolydian
3. A dorian
4. E aeolian
5. B phrygian
6. F# locrian
7. G melodic minor
8. A melodic minor second mode
9. C lydian augmented
10. C lydian dominant
11. D melodic minor fifth mode
12. E locrian #2
13. F# altered
14. A composite blues
15. C composite blues
16. D composite blues
17. A dorian #4
18. E harmonic minor
19. B neopolitan minor
20. A romanian minor
21. A# diminished
22. C# diminished
23. E diminished
24. G diminished
25. C hungarian major
26. B spanish
27. B spanish heptatonic
28. F# flamenco
29. A kafi raga
30. D bebop
31. G bebop
32. D bebop dominant
33. G bebop dominant
34. A bebop minor
35. D bebop minor
36. G bebop major
37. B bebop locrian
38. F# bebop locrian
39. E minor bebop
40. G# enigmatic
41. E minor six diminished
42. G minor six diminished
43. G ionian augmented
44. C lydian #9
45. C ichikosucho
46. G ichikosucho

[*] Please enter the corresponding number for the scale you want to see on the fretboard, or 'n' to exit: 3

0. (6-String Guitar) E standard
1. (6-String Guitar) Drop D
2. (6-String Guitar) D standard
3. (6-String Guitar) Drop C
4. (6-String Guitar) Drop B
5. (6-String Guitar) Drop A
6. (6-String Guitar) Open D
7. (6-String Guitar) Open G
8. (6-String Guitar) Open C
9. (7-String Guitar) Standard
10. (7-String Guitar) Drop A
11. (4-String Bass) E standard
12. (4-String Bass) Drop D
13. (4-String Bass) D standard
14. (4-String Bass) Drop C
15. (4-String Bass) Drop B
16. (4-String Bass) Drop A
17. (5-String Bass) E standard
18. (5-String Bass) Drop D
19. (5-String Bass) D standard
20. (5-String Bass) Drop C
21. (5-String Bass) Drop B
22. (5-String Bass) Drop A
'
[*] Please select the tuning to use:  0

[Tuning: (6-String Guitar) E standard] ['E', 'A', 'D', 'G', 'B', 'E']
Scale: [A dorian] 
Formula: [1 2 3b 4 5 6 7b] 
Notes: ['A', 'B', 'C', 'D', 'E', 'F#', 'G']

 Str  |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |  10  |  11  |  12  |
 -E-  |--E---|------+--F#--+--G---+------+--A---+------+--B---+--C---+------+--D---+------+--E---+
 -B-  |--B---|--C---+------+--D---+------+--E---+------+--F#--+--G---+------+--A---+------+--B---+
 -G-  |--G---|------+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+--G---+
 -D-  |--D---|------+--E---+------+--F#--+--G---+------+--A---+------+--B---+--C---+------+--D---+
 -A-  |--A---|------+--B---+--C---+------+--D---+------+--E---+------+--F#--+--G---+------+--A---+
 -E-  |--E---|------+--F#--+--G---+------+--A---+------+--B---+--C---+------+--D---+------+--E---+

[Scale Chords]
   Triad Notes:   Scale Degrees:
1 ['A', 'C', 'E'] [1, 3, 5]
2 ['B', 'D', 'F#'] [2, 4, 6]
3 ['C', 'E', 'G'] [3, 5, 7]
4 ['D', 'F#', 'A'] [4, 6, 1]
5 ['E', 'G', 'B'] [5, 7, 2]
6 ['F#', 'A', 'C'] [6, 1, 3]
7 ['G', 'B', 'D'] [7, 2, 4]
```

# Requirments
Python 3.x or higher

# Setup 
```   
    > git clone https://github.com/metaevolution/ScaleFinder.git
    > cd ScaleFinder
    > python3 setup.py install
```
Or using Virtualenv
```   
    > python3 -m virtualenv .venv
    > source  .venv/bin/activate
    > git clone https://github.com/metaevolution/ScaleFinder.git
    > cd ScaleFinder
    > python3 setup.py install
```



# Tests 
```
python3 -m unittest tests/*.py
```





