General notes on using MML in archeage

* If 64th notes are present, the tempo must be divisbile by 6. This includes dotted 32nd notes or staccato 32nd notes.

* Default archeage volume is 100 (v100).  Max is 127 (v127).

* Default note length is 4 (l4).  If any track changes the length, all following tracks inherit that length. 3MLE assumes that following tracks default back to l4. So when optimizing, it's critical to start any track following a note length change with l4 if it doesn't start with a length.

* All explicitly written octaves in the 3MLE code must be increased by 1.  I.e., if 3MLE exports "o4", change this to "o5" for archeage.

* Some of the guidance [here](https://www.reddit.com/r/archebards/comments/3bwgj7/howto_fix_archeagemml_desyncs/) is incorrect, but useful.

* Any tempo changes must only be done in the first track.  All other tracks will inherit them automatically.  If there are tracks outside of track one that do tempo changes, good luck.

* Archeage does not work with optimized "n" notes.  These need to be converted back to the corresponding note. A simple program can do this, if you have a zero based array that goes starts with "c" and goes up to "b".  The converted n note is the modulus 12 of the number.  I.e., n32 is g+ (32 % 12 = 8). 8 is the 9th element of a zero based array, which would be g sharp/a flat. See the midi-note.pl perl script as an example.

* Arpeggiated chords can generally be represented by using 32nd note rests between each member of the chord.  The lowest note would have its full length, the second note would start with a 32nd note rest, followed by the rest of the duration, the 3rd note with a 16th note rest (32nd rest twice) and then the rest of the duration, etc.  These obviously take one track per note, so a 3-note arpeggiated chord requires 3 tracks.  This works well with eigth note up to whole note arpeggiated chords.  For 16th note arpeggiated chords, 64th note rests need to be used.

