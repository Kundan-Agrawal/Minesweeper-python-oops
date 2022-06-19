from binhex import REASONABLY_LARGE
from tkinter import *
from turtle import bgcolor, color
import settings
import utility
from cell import Cell

root = Tk()
# Override the setting of the window
root.configure(bg='black')
# this is for the size of window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)  # this is used to stop resizing the window

top_frame = Frame(
    root,
    bg='black',  # change later to black
    width=settings.WIDTH,
    height=utility.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='green',
    text='Minesweeper Game',
    font=('', 30)
)
game_title.place(
    x=utility.width_prct(25), y=0
)

left_frame = Frame(
    root,
    bg="black",
    width=utility.width_prct(25),
    height=utility.height_prct(75)
)
left_frame.place(x=0, y=utility.height_prct(25))


center_frame = Frame(
    root,
    bg="black",
    width=utility.width_prct(75),
    height=utility.height_prct(75)

)
center_frame.place(
    x=utility.width_prct(25),
    y=utility.height_prct(25)
)


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x, y)
        c1.create_btn_object(center_frame)
        c1.cell_btn_object.grid(
            column=x, row=y
        )

# call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.ransomize_mines()


# rum the window
root.mainloop()
