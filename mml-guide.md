General notes on using MML in Archeage

* If 32nd or 64th notes are present, the tempo must be divisbile by 6. It is suggested when importing a MIDI into 3MLE to use 1/64th note Quantization.

* Default Archeage volume is 100 (v100).  Max is 127 (v127).

* Max tempo is 259 for Archeage

* Any tempo changes must only be done in the first track.  All other tracks will inherit them automatically.  If a tempo change is done outside of the first track, good luck as it will have odd consequences.

* Arpeggiated chords can generally be represented by using 64th note rests between each member of the chord.  The lowest note would have its full length, the second note would start with a 64th note rest, followed by the rest of the duration, the 3rd note with a 32nd note rest (64th rest twice) and then the rest of the duration, etc.  These obviously take one track per note, so a 3-note arpeggiated chord requires 3 tracks.  This works well with sixteenth note up to whole note arpeggiated chords.

* A trill is best done as 64th notes for the duration of the trilled note. Note that up until the time of Mozart and Haydn, a trill starts on the next higher note and drops to the trilled note in this rapid succession.  After that time, it starts on the indicated note and raises to the next higher note in rapid succession.

* Here is information on how to [represent tuplets](tuplets.md) properly in MML.

# 3MLE

* To create a drum track in 3MLE, add the following literal text to the first lines of the track:

```
    //#using_extension
    //#using_channel = 10
```

Use this [percussion map](https://computermusicresource.com/GM.Percussion.KeyMap.html) to help with creating drum tracks. You will need to move the specified note UP one octave (I.e., A3 should be A4) for the right drum instrument to be used in 3MLE.  The conversion script will correctly handle this when the track(s) are processed.

The following items are all fixed by using the [3mle-archeage.py script](https://raw.githubusercontent.com/kernighan/archeage-3mle/main/3mle-archeage.py) script to process MML exported by 3MLE in Mabinogi format. The documentation is in the [README](README.md) file.

*  Volume (velocity) conversion from 3MLE to Archeage along with [musical dynamics notation](https://en.wikipedia.org/wiki/Dynamics_%28music%29#Interpretation_by_notation_programs)

| 3MLE | Archeage |Notation|
| ---- | -------- |--------|
| v0   | v0       |        |
| v1   | v8       |        |
| v2   | v16      | ppp    |
| v3   | v24      |        |
| v4   | v32      | pp     |
| v5   | v40      |        |
| v6   | v48      | p      |
| v7   | v56      |        |
| v8   | v64      | mp     |
| v9   | v72      |        |
| v10  | v80      | mf     |
| v11  | v88      |        |
| v12  | v96      | f      |
| v13  | v104     |        |
| v14  | v112     | ff     |
| v15  | v127     | fff    |

* Default note length is 4 (l4).  If any track changes the length, all following tracks inherit that length. 3MLE assumes that following tracks default back to l4, but Archeage does not. So when optimizing, it's critical to start any track following a note length change with l4 if it doesn't start with a length.

* All explicitly written octaves exported by 3MLE must be increased by 1.  I.e., if 3MLE exports "o4", change this to "o5" for Archeage.

* Archeage does not work with optimized "n" notes.  These need to be converted back to the corresponding note. A simple program can do this, if you have a zero based array that goes starts with "c" and goes up to "b".  The converted n note is the modulus 12 of the number.  I.e., n32 is g+ (32 % 12 = 8). 8 is the 9th element of a zero based array, which would be g sharp/a flat.


# Known bugs with 3MLE

* 3MLE fails to import tuplets correctly.  For example, an 8th note triplet should be a length of 12.  For example, if it was desired to have 8th note triplets of abc, it should be:

> a12b12c12

However, 3MLE will import this as:

> a16&a64b16.c16&c64

* 3MLE will sometimes create an optimization like:

> b&l16b

This does not work in Archeage, and must be rewritten as:

> b&b16l16

Until the script is fixed to handle this special case
