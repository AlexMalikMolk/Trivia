from tkinter import Tk, Label


class Highscore:
    def __init__(self):
        self.window = Tk()
        self.window.title("Highscore")
        self.window.geometry("850x530")

        # load data from score.txt

        self.load_data()

    def load_data(self):
        # Open the score.txt file in read mode
        with open('score.txt', 'r') as file:
            # Read the contents of the file
            data = file.read()

        # Split the data into lines
        lines = data.split('\n')

        # Initialize the y coordinate for the labels
        y = 50

        # Iterate over the lines
        for line in lines:
            # Get the name and score from the line
            name, score = line.split(',')

            # Create a label to display the name
            name_label = Label(self.window, text=name, justify='left')
            # placing the label in the window
            name_label.place(x=50, y=y)

            # Create a label to display the score
            score_label = Label(self.window, text=score, justify='right')
            # placing the label in the window
            score_label.place(x=600, y=y)

            # Increment the y coordinate for the next label
            y += 50

            # change font size
            name_label.config(font=("Arial", 16, "bold"))
            score_label.config(font=("Arial", 16, "bold"))
