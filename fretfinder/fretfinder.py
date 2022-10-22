

class FretFinder():

    def __init__(self, scales):
        self.notes = []
        self.scales = scales

    def add_note(self, note):
        self.notes.append(note)

    def results(self):
        return self.scales.search(self.notes)