Tools for use with Archeage and 3MLE

There are several tools here, but only one is really needed, [3mle-archeage.py](https://raw.githubusercontent.com/kernighan/archeage-3mle/main/3mle-archeage.py).

Current version: 1.0.4, released July 27, 2022

The 3mle-archeage.py (3mle-archeage.cgi) is a python3 script that takes MML as exported in 3MLE via the "Export MML to clipboard" option from the File menu and converts it for use with Archeage (legacy or unchained).  It is expected that the supplied MML is a single continuous block of all the tracks, which means some editing will be necessary if there are more than 3 tracks to the song, since 3MLE will only export 3 tracks at a time.

If the script is installed with the name "3mle-archeage.cgi" it will act as a CGI script for a webserver.  The 3mle-archeage.html file is an example HTML form page that can be used to take input for processing.  This has not yet been tested, feel free to report issues if attempting to set this up on a webserver.

When run locally via the command line, it can take the following options:

1. --version - This will print the current version of the program
2. --nooctave - This will disable fixing the octaves in the song for Archeage. It is not advised to use this option.
3. --novolume - This will disable remapping Mabinogi velocities (volumes) for use with Archeage. It is not advised to use this option.
4. --volinc <integer> - Change the Mabinogi velocity (volume) by the provided integer before remapping them. A positive integer will increase the velocities, a negative integer will decrease them.
5. --octaveinc <integer> - Adjust the octave by the provided integer.  A positive integer will increase the octaves, a negative one will decrease them. Require --nooctave flag to be passed as well.
6. --infile <file> - A file with the MML code to read in for processing.  If this option is not specified, a prompt for the MML will be used instead.


To use on Windows 10:

1. Download the python script somewhere
2. Start a command prompt window
3. Change to the diretory where the script is
4. python 3mle-archage.py -f file.txt OR python 3mle-archage.py to get prompted for the MML code

Note: If python is not currently installed, just run the command "python" from the command prompt window, and the microsoft store will start up and it can be installed from there.

Note: There is at least one report that with Python 3.10 the program may crash if using the input mode rather than the file option.


Other files in this directory:

1. length-test.txt, length-fixed.txt - MML to test the length fix done by 3mle-archeage.py
2. macarena-opt.txt, macarena-no-octave.txt, macarena-octave.txt - MML to test the "n" note conversions and if the octave conversion is done correctly.
3. midi-note.pl, midi-note.py - Scripts to convert "n" notes to their corresponding MML note. Obsoleted by 3mle-archeage.py

See the [MML guide](mml-guide.md) for additional tips and tricks
