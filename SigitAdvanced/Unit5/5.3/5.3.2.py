class MusicNotes:
    def __init__(self):
        self._note_freqs = {'La': 55, 'Si': 61.74, 'Do': 65.41, 'Re': 73.42, 'Mi': 82.41, 'Fa': 87.31, 'Sol': 98}
        self._notes = iter(self._note_freqs.keys())
        self._octave = 0
        self._stop_freq = 1568

    def __iter__(self):
        return self

    def __next__(self):
        try:
            note = next(self._notes)
        except StopIteration:
            self._octave += 1
            self._notes = iter(self._note_freqs.keys())
            note = next(self._notes)

        freq = self._note_freqs[note] * (2 ** self._octave)
        if freq > self._stop_freq:
            raise StopIteration

        return freq

notes_iter = iter(MusicNotes())

for freq in notes_iter:
    print(freq)