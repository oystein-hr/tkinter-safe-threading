# tkinter-safe-threading-2-7
Example of safe threading with Tkinter

# Info
This code is a modified version of a [recipe on ActiveState][1], created by Jacob Hallén. It is made for
and tested on `python 2.7.11`.

#### Modifications
Want to keep this example as small and simple as possible, so only doing minimal modifications. I was
interested in seeing how to update the GUI while running a process in a thread.

- Instead of printing the randomnumber, I made it change the button text.
- Added a `minsize` to the window, so it doesn't resize as the button recieves new text.
- Added a binding to the `<Destroy>` event of the `root` window, so it stops
the thread if the window is closed.
- Function and variable names were modified to recommendations from PEP8.

#### Not PEP8
I use 120 characters per line instead of the PEP8 recommendation of 80.

#### Disclaimer
I am fairly new to python, so I can not guarantee that this code works safely. However, I will update it
if I learn anything is wrong with the code.


[1]: (http://code.activestate.com/recipes/82965-threads-tkinter-and-asynchronous-io/)