"""
   Quiz runner V0.74
   By Steve Shambles
   Oct 2020
   stevepython.wordpress.com

V0.72-Added option to play an mp3 for each question or not.
      mp3 must be named questionnumber.mp3, i.e 1.mp3, 12.mp3 etc.
      and stored in music-q folder.
V0.61-fixed 4 blank lines bug, not required now in answers file.
V0.61-a: images now need to be placed in the  'images' folder.
"""
import os
import random
import sys
from tkinter import Button, Frame, Label, LabelFrame, Menu
from tkinter import messagebox, PhotoImage, Tk, W
import webbrowser

import cv2
from pygame import mixer

mixer.init()


class Bg:
    """Variables, set at defaults for global use.
        add Bg. to each var then its global."""
    total_questions = 0
    your_score = 0
    qcount = 1
    answr_count = 0
    answer = ''
    wrong = ''
    choy = ''
    quest_frame = None
    ans_choices_frame = None
    your_rating = 0
    pc = 0
    window_title = ''
    high_score = 0
    ans_list = []
    music_q = False


root = Tk()
root.eval('tk::PlaceWindow . Center')
root.resizable(False, False)

# Check high_score.txt available, if not create it.
check_file = os.path.isfile('high_score.txt')
if not check_file:
    with open('high_score.txt', 'w') as contents:
        pass


def save_high_score():
    """Save high score to file in current dir."""
    with open('high_score.txt', 'w') as contents:
        save_it = str(Bg.high_score)
        contents.write(save_it)


def load_high_score():
    """Load in text file containing players best score."""
    with open('high_score.txt', 'r') as contents:
        saved_high_score = contents.read()
        if saved_high_score > '':
            Bg.high_score = int(saved_high_score)


def quit_prg():
    """Create askyn msg box for quitting program."""
    ask_quit = messagebox.askyesno('Quit the quiz?',
                                   'Are you sure you\n'
                                   'want to exit?')
    if ask_quit is True:
        root.destroy()
        stop_music()
        sys.exit()


def file_checks():
    "Check for existence of essentila files."""
    mf_msg = ''

    if not os.path.isfile('settings.txt'):
        mf_msg = 'The file:\nsettings.txt\nis missing.'
    if not os.path.isfile('questions.txt'):
        mf_msg = 'The file:\nquestions.txt\nis missing.'
    if not os.path.isfile('answers.txt'):
        mf_msg = 'The file:\nanswers.txt\nis missing.'
    if not os.path.isfile('quiz-logo-450x253.png'):
        mf_msg = 'The file:\nquiz-logo-450x253.png\nis missing'
    if not os.path.isfile('quiz-help.txt'):
        mf_msg = 'The file:\nquiz-help.txt\nis missing'

    if not mf_msg:
        return

    root.withdraw()
    messagebox.showerror('Warning', (mf_msg) + '\n'
                         'Cannot continue.')
    root.destroy()
    sys.exit()


# Check for essential files.
file_checks()

# Load in variables from settings.txt.
# There will be more in future updates.
with open('settings.txt', 'r') as f:
    Bg.window_title = f.readline()
    Bg.window_title = Bg.window_title.rstrip('\n')

# Load questions into a list called quest_list.
with open('questions.txt', 'r') as f:
    # splitlines removes the newline esc char.
    ques_list = f.read().splitlines()

# Find out how many questions were loaded in.
Bg.total_questions = (len(ques_list))

# Load multiple choice answers into Bg.ans_list.
with open('answers.txt', 'r') as f:
    Bg.ans_list = f.read().splitlines()


def play_music():
    """Play background music."""
    if os.path.isfile('sqm.mp3'):
        mixer.music.load('sqm.mp3')
        mixer.music.play(-1)  # Play indefinetly -1. 0 or () = play once.


def stop_music():
    """Stop music playing."""
    mixer.music.stop()


def get_rating():
    """Get percentage of questions answered correctly
        and link it to a game over message."""
    Bg.your_rating = 0
    per_cent = 100 * float(Bg.your_score)/float(Bg.total_questions)
    temp = round(per_cent, 3)
    Bg.pc = str(temp)+'%'

    if per_cent < 26:
        Bg.your_rating = 'This score sucks, are you for real?'
        return
    if per_cent < 51:
        Bg.your_rating = 'An OK score I guess.'
        return
    if per_cent < 76:
        Bg.your_rating = 'Hey, that is a pretty good score.'
        return
    if per_cent < 101:
        Bg.your_rating = 'OMG a true genius. Now go and get a life okay!'
        return


def check_end_game():
    """Check if game over, if so get rating and end game."""
    get_rating()

    if Bg.qcount > Bg.total_questions:
        messagebox.showinfo(Bg.window_title, 'Game Over\n\nYou scored '
                            + str(Bg.your_score) + ' out of '
                            + str(Bg.total_questions) + '\n\n'
                            + str(Bg.your_rating))
        root.destroy()
        stop_music()
        sys.exit()

    # stop previous music question playing.
    if Bg.music_q:
        stop_music()
        Bg.music_q = False


def update_score():
    """Update the players score label."""
    score_label = Label(score_frame,
                        bg='orange',
                        font=('Helvetica', 14, 'bold'),
                        text='Your Score: ' + str(Bg.your_score) +
                        '    Highscore: ' + str(Bg.high_score))
    score_label.grid(row=0, column=0, pady=14)


def correctly_answered():
    """Pop up box if answered correctly."""
    messagebox.showinfo(Bg.window_title,
                        str(Bg.answer) + ' is correct\n\n'
                        'Well done, you earned a point.')
    Bg.qcount += 1  # Next question.
    Bg.answr_count += 4

    # Update highscore.
    if Bg.your_score > Bg.high_score:
        Bg.high_score = Bg.your_score
        save_high_score()
        update_score()

    check_end_game()
    display_quest_count()
    display_question()
    display_answer_choices()


def wrong_answer():
    """Pop up box if answered incorrectly."""
    messagebox.showinfo(Bg.window_title,
                        str(Bg.wrong) + ' is wrong\n\n'
                        'You get no points for that.')
    Bg.qcount += 1
    Bg.answr_count += 4
    check_end_game()
    display_quest_count()
    display_question()
    display_answer_choices()


def display_quest_count():
    """Show question number."""
    qcount_label = Label(qcount_frame,
                         bg='indianred',
                         fg='white',
                         font=('Helvetica', 14, 'bold'),
                         text='Question ' + str(Bg.qcount) + ' of '
                         + str(Bg.total_questions))
    qcount_label.grid(row=1, column=0)


def music_question():
    """Play music question if mp3 present for current question."""
    mp3 = 'music-q/' + str(Bg.qcount) + '.mp3'

    if os.path.isfile(mp3):
        stop_music()
        mixer.music.load(mp3)
        mixer.music.play()  # Play indefinetly -1. 0 or () = play once.
        Bg.music_q = True
    else:
        Bg.music_q = False
        # play_music()


def display_question():
    """Display question."""
    Bg.quest_frame.destroy()
    Bg.quest_frame = Frame(root)
    Bg.quest_frame.grid(row=2, column=0, padx=5, pady=8)

    quest_ion = (ques_list[Bg.qcount-1])
    quest_label = Label(Bg.quest_frame,
                        height=3,
                        fg='blue',
                        wraplength=330,
                        justify='left',
                        font=('Helvetica', 11, 'italic', 'bold'),
                        text='Q. ' + quest_ion)
    quest_label.grid(row=0, column=0)

    # Load and display image if there is one linked to question.
    logo_lbl = Label(logo_frame)
    img = 'images/' + str(Bg.qcount) + '.png'

    if os.path.isfile(img):
        # Resize image.
        bg_img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        width = 450
        height = 253
        dim = (width, height)
        resized = cv2.resize(bg_img, dim, interpolation=cv2.INTER_AREA)
        # Save resized img tremporarily.
        cv2.imwrite('temp.png', resized)
        # Display img.
        logo_lbl = Label(logo_frame)
        PHOTO = PhotoImage(file='temp.png')
        logo_lbl.config(image=PHOTO)
        logo_lbl.grid(row=0, column=0, padx=2, pady=2)
        logo_lbl.photo = PHOTO
    # No user img to load so revert to logo.
    else:
        load_display_logo()

    # Check if is music question, if so play.
    music_question()


def display_answer_choices():
    """Show the multiple choice answers."""
    correct_answer = Bg.answr_count

    Bg.ans_choices_frame.destroy()
    Bg.ans_choices_frame = Frame(root)
    Bg.ans_choices_frame.grid(row=3, column=0, padx=5, pady=8)

    # Need to get the four multiple choice answers into a list so
    # that the answers can be shuffled randomly
    temp1 = Bg.ans_list[Bg.answr_count]
    temp2 = Bg.ans_list[Bg.answr_count + 1]
    temp3 = Bg.ans_list[Bg.answr_count + 2]
    temp4 = Bg.ans_list[Bg.answr_count + 3]

    # Have to join like this, I dont know other way to do it,
    # but doing it this way makes a tuple which cant be shuffled.
    tup = (temp1), (temp2), (temp3), (temp4)

    # So convert tuple to a list, otherwise can't shuffle it
    Bg.choy = list(tup)

    # Mix up the sequence of answers because in Bg.ans_list the correct
    # answer is always first.
    random.shuffle(Bg.choy)

    # Print the answer choices, now that they are in a random order.
    ans_0 = Label(Bg.ans_choices_frame,
                  font=('Helvetica', 10, 'bold'),
                  text='A. ' + Bg.choy[0])
    ans_0.grid(row=0, column=0, sticky=W)

    ans_1 = Label(Bg.ans_choices_frame,
                  font=('Helvetica', 10, 'bold'),
                  text='B. ' + Bg.choy[1])
    ans_1.grid(row=1, column=0, sticky=W)

    ans_2 = Label(Bg.ans_choices_frame,
                  font=('Helvetica', 10, 'bold'),
                  text='C. ' + Bg.choy[2])
    ans_2.grid(row=2, column=0, sticky=W)

    ans_3 = Label(Bg.ans_choices_frame,
                  font=('Helvetica', 10, 'bold'),
                  text='D. ' + Bg.choy[3])
    ans_3.grid(row=3, column=0, sticky=W)

    Bg.answer = Bg.ans_list[correct_answer]


def clkd_but_a():
    """Answer button A was clicked."""
    if Bg.answer == Bg.choy[0]:
        Bg.your_score += 1
        update_score()
        correctly_answered()
    else:
        Bg.wrong = Bg.choy[0]
        wrong_answer()


def clkd_but_b():
    """Answer button B was clicked."""
    if Bg.answer == Bg.choy[1]:
        Bg.your_score += 1
        update_score()
        correctly_answered()
    else:
        Bg.wrong = Bg.choy[1]
        wrong_answer()


def clkd_but_c():
    """Answer button C was clicked."""
    if Bg.answer == Bg.choy[2]:
        Bg.your_score += 1
        update_score()
        correctly_answered()
    else:
        Bg.wrong = Bg.choy[2]
        wrong_answer()


def clkd_but_d():
    """Answer button D was clicked."""
    if Bg.answer == Bg.choy[3]:
        Bg.your_score += 1
        update_score()
        correctly_answered()
    else:
        Bg.wrong = Bg.choy[3]
        wrong_answer()


def display_help_text():
    """Show help text in a scrolled text box in a child window."""
    webbrowser.open('quiz-help.txt')


def about_menu():
    """Msgbox Info about this program."""
    messagebox.showinfo(Bg.window_title,
                        Bg.window_title +
                        '\n\nwas created with\n'
                        'Simple Quiz Maker,\n'
                        'Freeware 2020.\n\n'
                        'Available from:\n'
                        'stevepython.wordpresss.com')


def load_display_logo():
    """Load and display default logo image."""
    root.title(Bg.window_title)
    logo_lbl = Label(logo_frame)
    PHOTO = PhotoImage(file='quiz-logo-450x253.png')
    logo_lbl.config(image=PHOTO)
    logo_lbl.grid(row=0, column=0, padx=2, pady=2)
    logo_lbl.photo = PHOTO


def start_screen():
    """pop up msgbox to delay start so can display default logo first."""
    messagebox.showinfo(Bg.window_title,
                        'Click OK to start the Quiz.')
    play_music()


# Frame for logo display.
logo_frame = LabelFrame(root, width=454, height=253,
                        text=Bg.window_title)
logo_frame.grid(row=0, column=0)

load_display_logo()
start_screen()

# Frame for question counter.
qcount_frame = Frame(root)
qcount_frame.grid()

# Frame for printing questions.
Bg.quest_frame = Frame(root)
Bg.quest_frame.grid(row=2, column=0, padx=5, pady=8)

# Frame for printing the 4 poss answer choices in.
Bg.ans_choices_frame = Frame(root)
Bg.ans_choices_frame.grid(row=3, column=0, padx=5, pady=8)

# Frame for the answer buttons.
btns_frame = LabelFrame(root, bg='powderblue')
btns_frame.grid(padx=5, pady=8)

# Frame for score counter.
score_frame = Frame(root)
score_frame.grid()

# GUI buttons A B C D.
btn0 = Button(btns_frame,
              bg='gold',
              font=('Helvetica', 14, 'bold'),
              text=' A ',
              command=clkd_but_a)
btn0.grid(row=5, column=0, pady=15, padx=15)

btn1 = Button(btns_frame,
              bg='red',
              font=('Helvetica', 14, 'bold'),
              text=' B ',
              command=clkd_but_b)
btn1.grid(row=5, column=1, pady=15, padx=15)

btn2 = Button(btns_frame,
              bg='springgreen',
              font=('Helvetica', 14, 'bold'),
              text=' C ',
              command=clkd_but_c)
btn2.grid(row=5, column=2, pady=15, padx=15)

btn3 = Button(btns_frame,
              bg='white',
              font=('Helvetica', 14, 'bold'),
              text=' D ',
              command=clkd_but_d)
btn3.grid(row=5, column=3, pady=15, padx=15)


# Drop-down menu.
MENU_BAR = Menu(root)
FILE_MENU = Menu(MENU_BAR, tearoff=0)
MENU_BAR.add_cascade(label='Menu', menu=FILE_MENU)
FILE_MENU.add_command(label='Help', command=display_help_text)
FILE_MENU.add_command(label='About', command=about_menu)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Play music', command=play_music)
FILE_MENU.add_command(label='Stop music', command=stop_music)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Exit', command=quit_prg)
root.config(menu=MENU_BAR)

# Start game.
load_high_score()
display_quest_count()
display_question()
music_question()
display_answer_choices()
update_score()

root.protocol("WM_DELETE_WINDOW", quit_prg)

root.mainloop()
