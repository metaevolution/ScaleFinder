from fretfinder import FretFinder

if __name__ == "__main__":

    note1 = "F#"
    note2 = "B"
    note3 = "G"

    ff = FretFinder()

    ff.add_note(note1)
    print(ff.results())

    ff.add_note(note1)
    print(ff.results())

    ff.add_note(note1)
    print(ff.results())


