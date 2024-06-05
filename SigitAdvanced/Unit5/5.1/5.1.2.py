import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392
         }
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

notes_list = notes.split('-')
print(notes_list, '\n')

for note in notes_list:
    note_info = note.split(',')
    print(note_info)
    note_name = note_info[0]
    duration = int(note_info[1])

    winsound.Beep(freqs[note_name], duration)