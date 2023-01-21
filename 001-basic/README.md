# Basic Sequencer

Create a basic sequencer with two tracks, 16 steps per track.

Implementing this on a Raspberry Pi Pico with a Pimoroni Scroll (17x7
white LED matrix with 4 buttons).

The sequencer has 2 tracks with 16 notes each and runs at a fixed 120
bpm. The board has buttons on GPIO pins 12, 13, 14, and 15; they move
the cursor left, move the cursor right, toggle the currently selected
note on track 0, and toggle the currently selected note on track 1
respectively.

The two tracks control LEDs that are connect on GPIO pins 6 and
7. When the current note on the respective track is on, the LED is
turned on by driving the pin low, otherwise the LED is turned off by
driving the pin high.