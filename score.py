from tkinter import Tk, Label


class Highscore:
    def __init__(self):
        self.window = Tk()
        self.window.title("Highscore")
        self.window.geometry("850x530")

        # black background and white bold text arial font 16
        self.window.config(bg="black")
        self.window.option_add("*Font", "arial 16 bold")
        self.window.option_add("*Foreground", "white")

        # load data from score.txt and display it
        self.load_data()

    def load_data(self):
        # Open the score.txt file in read mode
        with open('score.txt', 'r') as file:
            # Read the contents of the file
            data = file.read()

        # Create a label to display the data
        label = Label(self.window, text=data)
        label.pack()


