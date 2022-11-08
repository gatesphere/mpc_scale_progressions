#!/usr/bin/env python3

# mpc_scale_progressions.py
#
# Creates an MPC-compatible .progression files for given scales
#
# github.com/gatesphere 2022
# Released without warranty into the public domain
#
# usage:
#   First, edit the 'SCALES' dictionary below,
#   then simply run the script with python 3.
#   .progression files will be created in the same 
#   directory as the script.

import json

# Define scales below, with 'C' as the root note.  MPC is smart 
# enough to transpose them to other roots.
# ex: 'Hirajoshi': ['C', 'D', 'Eb', 'G', 'Ab']

SCALES = {
  'Hirajoshi': ['C', 'D', 'Eb', 'G', 'Ab'],
  'Iwato': ['C', 'Db', 'F', 'Gb', 'Bb']
}


#########################################
#  don't edit anything below this line  #
#########################################

# maps note names to MIDI values in octave '2'
midi_notes = {
  'C': 48, 'C#': 49, 'Db': 49, 'D': 50, 'D#': 51, 'Eb': 51,
  'E': 52, 'F': 53, 'F#': 54, 'Gb': 54, 'G': 55, 'G#': 56,
  'Ab': 56, 'A': 57, 'A#': 58, 'Bb': 58, 'B': 59
}

# default formats
default_data = {
  'progression': {
    'name': 'TBD',
    'rootNote': 'C',
    'scale': 'Chromatic',
    'recordingOctave': 2,
    'chords': []
  }
}

note_format = {
  "name": "TBD",
  "role": "Normal",
  "notes": []
}

def main():
  for scale,notes in SCALES.items():
    # generate the file name
    fname = f'Scale-Scale{scale}.progression'

    # generate the progression name
    pname = f'Scale-Scale {scale}'

    # generate the note data
    note_data = []
    for n in notes:
      note = dict(note_format)
      note['name'] = n
      if n == 'C':
        note['role'] = "Root"
      note['notes'] = [midi_notes[n]]
      note_data.append(note)

    # make the output dict
    output_data = dict(default_data)

    # update the progression name
    output_data['progression']['name'] = pname

    # add the note data
    output_data['progression']['chords'] = note_data

    # json-ify it.
    with open(fname, 'w') as fh:
      json.dump(output_data, fh, indent=4)
    print(f'Wrote file "{fname}"')

if __name__=='__main__':
  main()
