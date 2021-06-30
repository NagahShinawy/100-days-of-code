"""
created by Nagaj at 26/06/2021
"""
import tkinter

from config import setup
from constants import *


def main():
    window = setup(
        title=MILES_TO_KM, image=IMAGE_TITLE_BAR, width=WINDOW_WIDTH, is_center=True
    )
    window.config(padx=5, pady=40)

    miles_to_km = tkinter.Label(text="Convert Miles to Km", font=("Arial", 15, "bold"))
    # expand=bool, it shows label in the center[center center] of window or make it just top center
    # side one of ==> [top, bottom, left, or right]
    # padding ==> padx, pady
    # miles_to_km.pack(
    #     expand=0, side=TOP, padx=MAIN_TITLE_XPAD, pady=MAIN_TITLE_YPAD
    # )  # show and center component(label) with custom features
    tkinter.Label(text="test").grid(row=0, column=0)
    btn = tkinter.Button(text="click Me")
    # btn.config(padx=50)
    btn.grid(row=0, column=2)
    btn2 = tkinter.Button(text="Attach")
    btn2.grid(row=1, column=1, padx=50)  # padding between components
    btn2.config(padx=30, pady=200)  # padding in the item itself between item text
    # tkinter.Button(text="ok").grid(row=1, column=2)
    tkinter.Entry().grid(row=2, column=3)
    # tkinter.Label().grid(row=2, column=3)
    # tkinter.Entry().grid(row=2, column=4)
    # add components to the window and keep me working
    #  keep window opens and listening to the user actions
    window.mainloop()  # keep window open while working


if __name__ == "__main__":
    main()
