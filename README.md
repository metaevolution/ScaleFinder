# ScaleFinder
## Quickly find a scale on the guitar by providing a few starting notes.

# Example Output
```
> python bin/scale_finder.py  -n "A B G# D E" 

[*] Found the following scales that include the notes ['A', 'B', 'G#', 'D', 'E']:

0. D lydian
1. A major
2. E mixolydian
3. B dorian
4. F# aeolian
5. C# phrygian
6. G# locrian
7. A melodic minor
8. B melodic minor second mode
9. C lydian augmented
10. D lydian dominant
11. E melodic minor fifth mode
12. F# locrian #2
13. G# altered
14. E mixolydian pentatonic
15. A minor hexatonic
16. B composite blues
17. D composite blues
18. E composite blues
19. D dorian #4
20. D lydian diminished
21. A harmonic minor
22. C# neopolitan minor
23. D romanian minor
24. A harmonic major
25. E spanish
26. C# spanish heptatonic
27. E spanish heptatonic
28. G# todi raga
29. B kafi raga
30. E kafi raga
31. D# purvi raga
32. D# persian
33. A bebop
34. E bebop
35. A bebop dominant
36. E bebop dominant
37. B bebop minor
38. E bebop minor
39. A bebop major
40. C bebop major
41. C# bebop locrian
42. G# bebop locrian
43. A minor bebop
44. F# minor bebop
45. A# enigmatic
46. A minor six diminished
47. C ionian augmented
48. A ichikosucho
49. D ichikosucho

[*] Found scales that include the notes ['A', 'B', 'G#', 'D', 'E']:

[*] Please enter the corresponding number for the scale you want to see on the fretboard, or 'n' to exit: 10

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

[Tuning: (6-String Guitar) E standard] [E, A, D, G, B, E]
[Scale: D lydian dominant ['D', 'E', 'F#', 'G#', 'A', 'B', 'C']]

 Str  |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |  10  |  11  |  12  |  13  |  14  |  15  |  16  |  17  |  18  |  19  |  20  |  21  |  22  |  23  |  24  |
 -E-  |--E---|------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+
 -B-  |--B---|--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+
 -G-  |------|--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+
 -D-  |--D---|------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+
 -A-  |--A---|------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+
 -E-  |--E---|------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+------+--F#--+------+--G#--+--A---+------+--B---+--C---+------+--D---+------+--E---+
```

# Requirments
Python 3.x or higher

# Setup 
```   
    > git clone https://github.com/metaevolution/ScaleFinder.git
    > cd ScaleFinder
    > python3 setup.py install
```

# Usage
```
    python3 bin/scale_finder.py  -h        
```
```      
    Usage: bin/scale_finder.py --notes A B C D F#
                
        INPUTS:

        -n, --notes:        Specify the notes you want to search relevant scales for. 
                            Separate multiple notes with spaces and surround with double quotes "". 
                            Use '#' for sharp, and 'b' for flat. e.g. 'Gb', 'A#' etc.
        -r, --root_note:    Limit suggestions to scales with the provided root note.

        DISPLAY:

        -d, --degrees:      Show scale degrees instead of note names. 
        -i, --invert:       Shows notes that are NOT in the selected scale.
        -x, --xo_mode:      Show 'O' instead of note letters, or pair with -i to show 'X' for notes not in the scale.

        MISC:

        -v, --verbose:      Enable verbose output
        -h, --help:         This help menu

```

# Tests 
```
python3 -m unittest tests/*.py
```





