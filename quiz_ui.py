from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from tkinter.simpledialog import askstring
from quiz_brain import QuizBrain
from score import Highscore

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.name = askstring("Ditt namn", "Vad heter du?:")

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Alex Frågesport")
        self.window.geometry("850x530")
        self.highscore = ()
        # Initialize the countdown timer
        self.count = 30

        # Display Title
        self.display_title()

        # Create a canvas for question text, and display question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Fråga här",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'arial', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Create a timer label
        self.timer_label = Label(self.window, text="", fg='black', font=('Helvetica', 24))

        # place the timer label
        self.timer_label.place(x=700, y=400)

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options (radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is right or wrong
        self.feedback = Label(self.window, pady=10, font=("arial", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Next, Quit and Score Button
        self.buttons()

        # start the timer and show it in the timer label
        self.countdown(self.count)

        # Mainloop
        self.window.mainloop()

    def countdown(self, count):
        # Update the label with the count
        self.timer_label.config(text=str(count))

        # Decrement the count
        count -= 1
        # If the count is greater than 0, call the function countdown and start the timer again from 30
        if count > 0:
            self.window.after(1000, self.countdown, count)
        else:

            # Popup showing to try again and restart the quiz
            messagebox.showinfo("Försök igen!", "Tryck på OK för att starta om programmet")
            # destroy the window
            self.window.destroy()
            # run the program again
            self.__init__(self.quiz)

    def display_title(self):

        # Title
        title = Label(self.window, text="Alex Frågesport",
                      width=50, bg="blue", fg="yellow", font=("arial", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    def display_question(self):
        # Display question

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):

        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(choice_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("arial", 14))

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=200, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return choice_list

    def display_options(self):
        # Display options

        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        # Check if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Rätt! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Fel! \n'
                                     f'Rätt svar är: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():

            # Moves to next to display next question and its options
            self.display_question()

            self.display_options()

            # Reset the timer to 30 and start the timer again
            self.count = 30
            self.timer_label.config(text="")
            self.countdown(self.count)

        else:
            # save the name and score_points of the user to score.txt delimited by a comma
            with open('score.txt', 'a') as file:
                file.write(f'{self.name},{self.quiz.score_points}\n')

            # if no more questions, then it displays the score
            self.display_result()

            # destroy the window
            self.window.destroy()

    def buttons(self):
        # define buttons

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self.window, text="Nästa", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("arial", 16, "bold"))

        # place the button on the screen
        next_button.place(x=350, y=460)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(self.window, text="Stäng", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("arial", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700, y=50)

        # Display the score
        highscore_button = Button(self.window, text="Poäng", command=self.score_btn, width=5, bg="red", fg="white",
                                  font=("arial", 16, " bold"))
        # Place button
        highscore_button.place(x=700, y=100)

    def score_btn(self):
        # if clicked on score button, then run Highscore class
        self.highscore = Highscore()

    def display_result(self):
        # Display the result
        correct, wrong, score_points = self.quiz.get_score()

        correct = f"Rätt: {correct}"
        wrong = f"Fel: {wrong}"

        # shows the points scored by the user

        result = f"Poäng: {score_points}"

        # Shows a message box to display the result
        messagebox.showinfo("Resultat", f"{result}\n{correct}\n{wrong}")
