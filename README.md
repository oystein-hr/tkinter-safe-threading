# tkinter safe threading
Example of safe threading with Tkinter.

- python 2.7.11
    - `2_7_example.py`
- python 3.5.1
    - `3_5_example.py`

# Info
This code is a modified version of a
[recipe on ActiveState](http://code.activestate.com/recipes/82965-threads-tkinter-and-asynchronous-io/)
, created by Jacob Hallén. Files are tested on OS X.

#### Modifications
Want to keep this example as small and simple as possible, so only doing minimal modifications. I was
interested in seeing how to update the GUI while running a process in a thread.

- Instead of printing the randomnumber, I made it change the button text.
- Added a `minsize` to the window, so it doesn't resize as the button recieves new text.
- Added a binding to the `<Destroy>` event of the `root` window, so it stops
the thread if the window is closed.
- Function and variable names were modified to recommendations from PEP8.

#### 2.7 vs 3.5
There aren't many differences in the code. Here are the differences.

- `import` module names
    - 2.7 have `Tkinter` and `Queue`
    - 3.5 have `tkinter` and `queue`
- other 3.5
    - Changed `GuiPart` argument from `queue` to `main_queue`, so it doesn't mix with
    the module named `queue`

#### Not PEP8
I use 120 characters per line instead of the PEP8 recommendation of 80.

#### Disclaimer
I am fairly new to python, so I can not guarantee that this code works safely. However, I will update it
if I learn anything is wrong with the code.
