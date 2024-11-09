from tkinter import * # to create Graphical User interfaces (GUIs) 
from PIL import Image, ImageTk #Python Image Library (PIL)
from random import choice # to generate computers random choice 
import time # for the timer 

class RockPaperScissorsGame:
    #__init__ method is declared within a class and is used to initialize the attributes of an object as soon as the object is formed
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.comp_score = 0
        self.round_time = 10  # round default time (secs)

        # initializing the root window
        self.root = Tk() # helps to display the root window and manages all the other components of the tkinter
        self.root.title("Python Mini Project : R.P.S")
        self.root.configure(background="#393E46")

        # to load images
        self.load_images()

        # creating frames ; we have used 3 (the start page, rules page and game page)
        self.create_start_frame()
        self.create_game_frame()
        self.create_instructions_frame()

    # load and resize images for rock, paper, and scissors for better graphics
    def load_images(self):
        self.rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").resize((175, 175)))
        self.paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((175, 175)))
        self.scissors_img = ImageTk.PhotoImage(Image.open("scissor.jpg").resize((175, 175)))

    # defining a function to create the interface of the start page
    def create_start_frame(self):
        self.start_frame = Frame(self.root, bg="#393E46")
        self.start_frame.grid(row=0, column=0, padx=250, pady=100)

        # title label
        title_label = Label(self.start_frame, text="Rock Paper Scissors", bg="#393E46", fg="#FFFFFF",
                            font=("Arial", 28, "bold"))
        title_label.pack(pady=20)

        # name label and entry
        name_label = Label(self.start_frame, text="Enter your name :", bg="#393E46", fg="#FFFFFF",
                           font=("Arial", 16))
        name_label.pack(pady=10)
        self.name_entry = Entry(self.start_frame, width=30, font=("Arial", 14))
        self.name_entry.pack(pady=20)

        # start game button
        start_button = Button(self.start_frame, width=20, height=3, text=" Start Game ", bg="#00ADB5", fg="#EEEEEE",
                              font=("Arial", 16, "bold"), relief=RIDGE, command=self.start_game)
        start_button.pack(pady=20)

        # instructions button
        instructions_button = Button(self.start_frame, width=15, height=2, text="Instructions", bg="#00ADB5", fg="#EEEEEE",
                                     font=("Arial", 16, "bold"), relief=RIDGE, command=self.show_instructions)
        instructions_button.pack(pady=10)

    # defining a function to create the interface of the game page
    def create_game_frame(self):
        self.game_frame = Frame(self.root, bg="#393E46")
        self.game_frame.grid(row=0, column=0, padx=100, pady=100)
        self.game_frame.grid_forget() # to hide the frame initially

        # user section
        user_in = Label(self.game_frame, font=("Arial", 26, "bold"), text="USER", bg="#393E46", fg="#EEEEEE")
        user_in.grid(row=0, column=1, pady=10)

        self.user_label = Label(self.game_frame, bg="#393E46")
        self.user_label.grid(row=1, column=1)

        self.user_name = Label(self.game_frame, text="", bg="#393E46", fg="#FFFFFF",
                               font=("Arial", 20, "bold"))
        self.user_name.grid(row=3, column=1)

        user_score_label = Label(self.game_frame, text="Score:", bg="#393E46", fg="#FFFFFF",
                                 font=("Arial", 16, "bold"))
        user_score_label.grid(row=4, column=1, pady=10)

        self.user_score_val = Label(self.game_frame, text="0", bg="#393E46", fg="#FFFFFF",
                                    font=("Arial", 16, "bold"))
        self.user_score_val.grid(row=5, column=1)

        # computer section
        comp_in = Label(self.game_frame, font=("Arial", 26, "bold"), text="COMPUTER", bg="#393E46", fg="#EEEEEE")
        comp_in.grid(row=0, column=3, pady=10)

        self.comp_label = Label(self.game_frame, bg="#393E46")
        self.comp_label.grid(row=1, column=3)

        comp_score_label = Label(self.game_frame, text="Score:", bg="#393E46", fg="#FFFFFF",
                                 font=("Arial", 16, "bold"))
        comp_score_label.grid(row=4, column=3, pady=10)

        self.comp_score_val = Label(self.game_frame, text="0", bg="#393E46", fg="#FFFFFF",
                                    font=("Arial", 16, "bold"))
        self.comp_score_val.grid(row=5, column=3)

        self.message = Label(self.game_frame, font=("Arial", 16, "bold"), bg="#393E46", fg="#FFFFFF")
        self.message.grid(row=6, columnspan=5, pady=20)

        # buttons for user choices
        rock = Button(self.game_frame, width=20, height=3, text="ROCK", bg="#00ADB5", fg="#EEEEEE",
                      font=("Arial", 16, "bold"), relief=RIDGE, command=lambda: self.update_choice("rock"))
        rock.grid(row=7, column=1, padx=10, pady=10)

        paper = Button(self.game_frame, width=20, height=3, text="PAPER", bg="#00ADB5", fg="#EEEEEE",
                       font=("Arial", 16, "bold"), relief=RIDGE, command=lambda: self.update_choice("paper"))
        paper.grid(row=7, column=2, padx=10, pady=10)

        scissors = Button(self.game_frame, width=20, height=3, text="SCISSORS", bg="#00ADB5", fg="#EEEEEE",
                          font=("Arial", 16, "bold"), relief=RIDGE, command=lambda: self.update_choice("scissors"))
        scissors.grid(row=7, column=3, padx=10, pady=10)

        # exit button
        exit_button = Button(self.game_frame, width=10, height=2, text="Exit", bg="#00ADB5", fg="#EEEEEE",
                             font=("Arial", 12, "bold"), relief=RIDGE, command=self.root.quit)
        exit_button.grid(row=8, column=0, columnspan=5, pady=20)

        # count down timer label
        self.timer_label = Label(self.game_frame, font=("Arial", 16, "bold"), bg="#393E46", fg="#FFFFFF")
        self.timer_label.grid(row=9, columnspan=5, pady=20)

    # defining a function to create the interface of the instruction page
    def create_instructions_frame(self):
        self.instructions_frame = Frame(self.root, bg="#393E46")
        self.instructions_frame.grid(row=0, column=0, padx=100, pady=100)
        self.instructions_frame.grid_forget()

        #  title label
        title_label = Label(self.instructions_frame, text="Instructions", bg="#393E46", fg="#FFFFFF",
                            font=("Arial", 28, "bold"))
        title_label.pack(pady=20)

        # rules label and text
        rules_label = Label(self.instructions_frame, text="Rules:", bg="#393E46", fg="#FFFFFF",
                            font=("Arial", 16, "bold"))
        rules_label.pack(pady=10)

        rules_text = "1. Choose either rock, paper, or scissors.\n" \
                     "2. The computer will also choose one.\n" \
                     "3. Rock beats scissors, scissors beats paper, and paper beats rock.\n" \
                     "4. The player with the higher choice wins the round and gets a point.\n" \
                     "5. The game continues until the player decides to exit.\n"

        rules_info = Label(self.instructions_frame, text=rules_text, bg="#393E46", fg="#FFFFFF",
                           font=("Arial", 14))
        rules_info.pack(pady=10)

        # back button
        back_button = Button(self.instructions_frame, width=10, height=2, text="Back", bg="#00ADB5", fg="#EEEEEE",
                             font=("Arial", 12, "bold"), relief=RIDGE, command=self.show_start_frame)
        back_button.pack(pady=20)

    def start_game(self):
                        try:
                            self.player_name = self.name_entry.get()
                            if self.player_name:
                                self.name_entry.delete(0, END)
                                self.user_name.configure(text=self.player_name)
                                self.start_frame.grid_forget()
                                self.game_frame.grid()

                                self.timer_seconds = 10  # set the countdown timer to 10 seconds initially
                                self.update_timer()
                            else:
                                raise ValueError("Please enter your name!")
                        except ValueError as e:
                            # a Label widget for the error message
                            self.error_message = Label(self.start_frame, text=str(e), fg="red", bg="#393E46", font=("Arial", 22, "bold"))
                            self.error_message.pack()

    def show_instructions(self):
        self.start_frame.grid_forget()
        self.instructions_frame.grid()

    def show_start_frame(self):
        self.instructions_frame.grid_forget()
        self.start_frame.grid()

    def update_choice(self, user_choice):
        comp_choice = choice(self.choices)
        self.display_choices(user_choice, comp_choice)
        self.update_scores(user_choice, comp_choice)

        # reset the timer after each choice update
        self.timer_seconds = 10

    def display_choices(self, user_choice, comp_choice):
        if user_choice == "rock":
            self.user_label.configure(image=self.rock_img)
        elif user_choice == "paper":
            self.user_label.configure(image=self.paper_img)
        else:
            self.user_label.configure(image=self.scissors_img)

        if comp_choice == "rock":
            self.comp_label.configure(image=self.rock_img)
        elif comp_choice == "paper":
            self.comp_label.configure(image=self.paper_img)
        else:
            self.comp_label.configure(image=self.scissors_img)

        # Animation for user and computer choices
        self.user_label.image = self.rock_img
        self.comp_label.image = self.rock_img
        self.animate_choice(self.user_label, user_choice)
        self.animate_choice(self.comp_label, comp_choice)

    def update_scores(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            self.message.configure(text="It's a tie!")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
                (user_choice == "paper" and comp_choice == "rock") or \
                (user_choice == "scissors" and comp_choice == "paper"):
            self.message.configure(text=f"{self.player_name} wins!")
            self.user_score += 1
            self.user_score_val.configure(text=str(self.user_score))

        else:
            self.message.configure(text="Computer wins!")
            self.comp_score += 1
            self.comp_score_val.configure(text=str(self.comp_score))

    def update_timer(self):
        if self.timer_seconds > 0:
            self.timer_label.configure(text=f"Time left: {self.timer_seconds} seconds")
            self.timer_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.message.configure(text="Time's up!")
            #self.timer_label.configure(text="Time left: 0 seconds")
           # rock.configure(state=DISABLED)
            #paper.configure(state=DISABLED)
            s#cissors.configure(state=DISABLED)
            
        

    def animate_choice(self, label, choice):
        if choice == "rock":
            image_sequence = [self.paper_img, self.scissors_img, self.rock_img]
        elif choice == "paper":
            image_sequence = [self.scissors_img, self.rock_img, self.paper_img]
        else:
            image_sequence = [self.rock_img, self.paper_img, self.scissors_img]

        for img in image_sequence:
            label.configure(image=img)
            label.image = img
            self.root.update()
            time.sleep(0.5)

    def run(self):
        self.root.mainloop()


game = RockPaperScissorsGame()
game.run()
