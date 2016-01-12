# -*- coding: utf-8 -*-
"""
This recipe describes how to handle asynchronous I/O in an environment where
you are running Tkinter as the graphical user interface. Tkinter is safe
to use as long as all the graphics commands are handled in a single thread.
Since it is more efficient to make I/O channels to block and wait for something
to happen rather than poll at regular intervals, we want I/O to be handled
in separate threads. These can communicate in a threasafe way with the main,
GUI-oriented process through one or several queues. In this solution the GUI
still has to make a poll at a reasonable interval, to check if there is
something in the queue that needs processing. Other solutions are possible,
but they add a lot of complexity to the application.

Original code created by Jacob Hallén, AB Strakt, Sweden. 2001-10-17
"""
import Tkinter
import time
import threading
import random
import Queue


class GuiPart:
    def __init__(self, master, queue, end_command):
        self.queue = queue
        self.master = master
        # Set up the GUI
        self.console = Tkinter.Button(self.master, text='Done', command=end_command)
        self.console.pack()
        # Add more GUI stuff here

    def process_incoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do what it says
                # As a test, we simply change the Button text
                self.console.configure(text=msg)

                # Update the window after changing text on Button
                self.master.update_idletasks()
            except Queue.Empty:
                pass


class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI. We spawn a new thread for the worker.
        """
        self.master = master

        # Create the queue
        self.queue = Queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.end_application)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = True
        self.thread1 = threading.Thread(target=self.worker_thread1)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodic_call()

        # If you close the window, stop the thread
        self.master.bind('<Destroy>', lambda event: self.end_application())

    def periodic_call(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        self.gui.process_incoming()
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(100, self.periodic_call)

    def worker_thread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select()'.
        One important thing to remember is that the thread has to yield
        control.
        """
        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following 2 lines with the real
            # thing.
            time.sleep(rand.random() * 0.3)
            msg = rand.random()
            self.queue.put(msg)

    def end_application(self):
        self.running = False

rand = random.Random()
root = Tkinter.Tk()
root.minsize(width=200, height=0)

client = ThreadedClient(root)
root.mainloop()
