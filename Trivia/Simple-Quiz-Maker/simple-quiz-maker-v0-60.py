"""Simple Quiz Maker V.060
   By Steve Shambles July 2020.
   stevepython.wordpress.com

   Module Dependencies:
   --------------------
   pip3 install opencv-python
   ttips.py in current dir.

   File dependencies:
   ------------------
   quiz-runner-v0-60.exe
   quiz-help.txt
   help.txt
   Must be found in same dir as SQM is run from.
   """
import os
import sys
from shutil import copyfile
import subprocess
from tkinter import Button, DISABLED, E, END, Entry, filedialog, Frame
from tkinter import INSERT, Label, LabelFrame, Menu, messagebox, N, NORMAL
from tkinter import PhotoImage, S, scrolledtext, Tk, Toplevel, W
import webbrowser

import cv2
import ttips


class Bg:
    """Variables, set at defaults for global use.
        add Bg. to each var then its global."""
    total_questions = 0
    your_score = 0
    qcount = 1
    answer = ''
    wrong = ''
    choy = ''
    quest_frame = None
    ans_choices_frame = None
    your_rating = 0
    pc = 0
    img = ''
    users_dir = ''
    E0 = ''
    E1 = ''
    E2 = ''
    E3 = ''
    qf_btn = ''
    af_btn = ''
    save_btn = ''
    test_btn = ''
    quiz_name_btn = None
    logo_btn = None
    accept_logo_btn = None
    orig_dir = os.getcwd()
    window_title = 'Simple Quiz Maker V0.60'
    open_folder_btn = None
    q_a_btn = ''

# Set up main window.
root = Tk()
root.title(Bg.window_title)
# root.geometry('462x740')
# root.eval('tk::PlaceWindow . Center')
# root.configure(borderwidth=4, relief='ridge')


def file_checks():
    "Check for existence of essential files."""
    mf_msg = ''

    if not os.path.isfile('quiz-runner-v0-60.exe'):
        mf_msg = 'The file quiz-runner-v0-60.exe is missing.'
    if not os.path.isfile('quiz-help.txt'):
        mf_msg = 'The file quiz-help.txt is missing.'
    if not os.path.isfile('help.txt'):
        mf_msg = 'The file help.txt is missing.'
    if not os.path.isfile('sqm-example-logo.png'):
        mf_msg = 'The file sqm-example-logo.png is missing.'

    if not mf_msg:
        return

    root.withdraw()
    messagebox.showerror('Warning', mf_msg)
    root.destroy()
    sys.exit()


# Check for essential files.
file_checks()

quiz_name_btn_frame = LabelFrame(root)
quiz_name_btn_frame.configure(borderwidth=2, relief='ridge')
quiz_name_btn_frame.grid(row=0, column=0, sticky=W+E)

# Frame for big yellow btn display.
load_logo_btn_frame = LabelFrame(root)
load_logo_btn_frame.configure(borderwidth=2, relief='ridge',
                              bg='limegreen')
load_logo_btn_frame.grid(row=1, column=0, sticky=W+E)

# Frame for logo display.
logo_frame = LabelFrame(root, width=454, height=253)
logo_frame.configure(borderwidth=2, relief='ridge',
                     bg='grey')
logo_frame.grid(row=2, column=0)

ttips.Create(logo_frame,
             'Your image will be auto resized\n'
             'if it is not 450x253 pixels.',
             fontname="helvetica",
             fontsize=12,
             showtime=12)

# Accept logo btn frame.
accept_logo_btn_frame = LabelFrame(root)
accept_logo_btn_frame.configure(borderwidth=2, relief='ridge',
                                bg='limegreen')
accept_logo_btn_frame.grid(row=4, column=0,sticky=W+E)

# Frame for inputs.
inputs_frame = LabelFrame(root)
inputs_frame.grid(row=5, column=0, pady=30)

# Finished_btn_frame.
finished_btn_frame = LabelFrame(root)
finished_btn_frame.configure(borderwidth=2, relief='ridge',
                                bg='indianred')
finished_btn_frame.grid(row=6, column=0, sticky=W+E)

# Music mesage frame.
music_msg_frame = LabelFrame(root)
music_msg_frame.configure(borderwidth=2, relief='ridge')
music_msg_frame.grid(row=7, column=0, sticky=W+E)
music_msg_lbl = Label(music_msg_frame,
                    font=('Helvetica', 11, 'bold'),
                    text='To add music to your quiz, copy an\n'
                         ' mp3 file to the sqm folder and '
                         'rename it sqm.mp3 ')
music_msg_lbl.grid(row=7, column=0, sticky=W+E)


def load_example_logo():
    logo_lbl = Label(logo_frame)
    PHOTO = PhotoImage(file='sqm-example-logo.png')
    logo_lbl.config(image=PHOTO)
    logo_lbl.grid(row=0, column=0, padx=2, pady=2)
    logo_lbl.photo = PHOTO


def create_dir():
    """Create folder for the files generated."""
    Bg.users_quiz_name = Bg.E0.get()

    if Bg.users_quiz_name == '':
        return

    Bg.users_dir = (Bg.users_quiz_name)
    check_dir = os.path.isdir(Bg.users_dir)

    if not check_dir:
        os.makedirs(Bg.users_dir)

        dest = Bg.users_dir+str(r'\quiz-runner-v0-60.exe')
        copyfile('quiz-runner-v0-60.exe', dest)

        dest2 = Bg.users_dir+str(r'\quiz-help.txt')
        copyfile('quiz-help.txt', dest2)

        dest3 = Bg.users_dir+str(r'\help.txt')
        copyfile('help.txt', dest3)

        os.chdir(Bg.users_dir)

        os.rename('quiz-runner-v0-60.exe', Bg.users_quiz_name+'.exe')

        #print('created folder : ', Bg.users_dir)
    else:
        fe_msg = str(Bg.users_dir) + '\nfolder already exists.\nPlease try a different name.'

        # os.chdir(Bg.users_dir)
        messagebox.showerror('Warning', fe_msg)
        return

    Bg.quiz_name_btn.configure(state=DISABLED)
    Bg.logo_btn.configure(state=NORMAL)
    Bg.E0.configure(state=DISABLED)


def ask_quiz_name():
    """Get name of users quiz to create."""
    Bg.quiz_name_btn = Button(quiz_name_btn_frame,
                              bg='gold',
                              font=('Helvetica', 11, 'bold'),
                              text='Step 1: Name your quiz below, '
                              'then click here',
                              command=create_dir)

    Bg.quiz_name_btn.grid(row=0, column=0, sticky=W+E, pady=15, padx=15)

    ttips.Create(Bg.quiz_name_btn,
                 'Fill in the input box below\n'
                 'with the name of your quiz\n'
                 'and then click here.',
                 fontname="helvetica",
                 fontsize=12,
                 showtime=10)

    Bg.E0 = Entry(quiz_name_btn_frame, bd=3)
    Bg.E0.grid(pady=5)
    Bg.E0.insert(0, 'Your quiz name')
    Bg.E0.focus()

    ttips.Create(Bg.E0,
                 'Type in the Name of your quiz\n'
                 'and then click the button above.',
                 showtime=10)
    return


def accept_logo():
    """Accept logo image supllied by user."""
    Bg.logo_btn.configure(state=DISABLED)
    Bg.accept_logo_btn.configure(state=DISABLED)
    Bg.qf_btn.configure(state=NORMAL)
    Bg.af_btn.configure(state=NORMAL)


def load_logo():
    """Allow user to load in their quiz logo image."""
    file_selected = filedialog.askopenfilename(title='Select image file',
                                               filetypes=[('All', '*.*')])

    if file_selected == '':
        return

    try:

        Bg.img = cv2.imread(file_selected, cv2.IMREAD_UNCHANGED)
        width = 450
        height = 253
        dim = (width, height)

        # Resize image.
        resized = cv2.resize(Bg.img, dim, interpolation=cv2.INTER_AREA)

    except:
        return

    # Save new image.
    cv2.imwrite('quiz-logo-450x253.png', resized)
    # Display image.
    logo_lbl = Label(logo_frame)
    PHOTO = PhotoImage(file='quiz-logo-450x253.png')
    logo_lbl.config(image=PHOTO)
    logo_lbl.grid(row=0, column=0, padx=2, pady=2)
    logo_lbl.photo = PHOTO

    accept_btn()


def accept_btn():
    """The accept image button."""
    # blanks = '' * 17
    Bg.accept_logo_btn = Button(accept_logo_btn_frame,
                                bg='gold',
                                font=('Helvetica', 11, 'bold'),
                                text='         Click here to use the above image            ',
                                command=accept_logo)
    
    Bg.accept_logo_btn.grid(row=4, column=0,
                            sticky=W+E,
                            pady=15, padx=15)

    ttips.Create(Bg.accept_logo_btn,
                 'Once clicked here your image is finalized.',
                 fontname="helvetica",
                 fontsize=12,
                 showtime=6)


def logo_load_btn():
    """The load logo button."""
    Bg.logo_btn = Button(load_logo_btn_frame,
                         bg='gold',
                         font=('Helvetica', 11, 'bold'),
                         text='         Step 2:'
                         'Click here to load a logo image     ',
                         command=load_logo)
    Bg.logo_btn.grid(row=1, column=0, sticky=W+E, pady=15, padx=15)

    ttips.Create(Bg.logo_btn,
                 'You can try out as many images as you want.\n'
                 'What you see is what you will get.',
                 fontname="helvetica",
                 fontsize=12,
                 showtime=14)


def load_questions():
    """File selector for user to load in their questions file."""
    qf_selected = filedialog.askopenfilename(title='Select your questions file',
                                             filetypes=[('Text', ('*.txt')),
                                                        ('All', '*.*')])
    if qf_selected:
        Bg.E1.delete(0, END)
        Bg.E1.insert(0, qf_selected)
        copyfile(qf_selected, 'questions.txt')
        ttips.Create(Bg.E1, qf_selected, showtime=10)
        Bg.qf_btn.configure(state=DISABLED)


def load_answers():
    """File selector for user to load in their answers file."""
    file_selected = filedialog.askopenfilename(title='Select your answers file',
                                               filetypes=[('Text', ('*.txt')),
                                                          ('All', '*.*')])
    if file_selected:
        Bg.E2.delete(0, END)
        Bg.E2.insert(0, file_selected)
        copyfile(file_selected, 'answers.txt')
        ttips.Create(Bg.E2, file_selected, showtime=10)

        Bg.save_btn.configure(state=NORMAL)
        Bg.test_btn.configure(state=NORMAL)
        Bg.af_btn.configure(state=DISABLED)
        #Bg.q_a_btn.configure(state=NORMAL)


def step_3():
    """The area where we display question and answers inputs
       and file selectors."""
    msg_lbl = Label(inputs_frame,
                    bg='gold',
                    font=('Helvetica', 11, 'bold'),
                    text='Step 3: Click both the ... buttons, '
                         'below right, \n'
                         'to load in your Question and Answers '
                         'text files.')
    msg_lbl.grid(row=5, columnspan=2)

    ttips.Create(msg_lbl,
                 'Available only when you have completed steps 1 and 2.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)

    Bg.E1 = Entry(inputs_frame, bd=3)
    Bg.E1.grid(pady=5)
    Bg.E1.insert(0, 'Your questions file')

    Bg.qf_btn = Button(inputs_frame, text='...', command=load_questions)
    Bg.qf_btn.grid(row=6, column=1)

    ttips.Create(Bg.E1,
                 'Please load your questions text file,\n'
                 'This file must be in the exact format described'
                 ' in the help file.\nSee drop down menu for help.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)

    ttips.Create(Bg.qf_btn,
                 'Click here to load your questions file',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)
    
    Bg.E2 = Entry(inputs_frame, bd=3)
    Bg.E2.grid(pady=5)
    Bg.E2.insert(0, 'Your answers file')

    Bg.af_btn = Button(inputs_frame, text='...', command=load_answers)
    Bg.af_btn.grid(row=7, column=1)

    ttips.Create(Bg.E2, 'Please load your answers text file,\n'
                 'This file must be in the exact format described'
                 ' in the help file.\nSee drop down menu for help.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)

    ttips.Create(Bg.af_btn,
                 'Click here to load your answers file',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)


def save_settings():
    """Store and save settings in user_vars list."""
    users_qu_file = Bg.E1.get()  # Not used at mo.
    users_an_file = Bg.E2.get()  # Not used at mo.
    quiz_name = Bg.users_dir

    user_vars = [quiz_name, users_qu_file, users_an_file]

    # Save users config settings.
    with open('settings.txt', 'w') as f:
        for user_var in user_vars:
            f.write(user_var)
            f.write('\n')

    Bg.open_folder_btn.configure(state=NORMAL)
    messagebox.showinfo('Program Information', 'Settings saved')


def quit_prg():
    """Create askyn msg box for quitting program"""
    ask_quit = messagebox.askyesno('Quit program?',
                                   'Are you sure you want\n'
                                   'to exit the program?.')

    if ask_quit is True:
        root.destroy()
        sys.exit()


def test_quiz():
    """Test run the created quiz."""
    save_settings()
    subprocess.Popen(Bg.users_quiz_name+'.exe')


def open_folder():
    """Open users folder using system default file browser."""
    user_fldr = os.getcwd()
    webbrowser.open(user_fldr)


def check_qa():
    """Future-update: Check questions against answers."""
    pass

    # Load questions into a list called quest_list.
    with open('questions.txt', 'r') as f:
        ques_list = f.read().splitlines()
        Bg.total_questions = (len(ques_list))
    # Load multiple choice answers into ans_list.
    with open('answers.txt', 'r') as f:
        ans_list = f.read().splitlines()
        separate = '-' * 40

    with open('qa-check.txt', 'w') as f:
        for check in range(len(ques_list)):
            ans_marker = check * 4
            print(ans_marker)
            f.write('Question: ' + str(check+1))
            f.write('\n')        
            f.write(ques_list[check])
            f.write('\n')
            f.write(ans_list[ans_marker])
            f.write('\n')
            f.write(separate)
            f.write('\n')

    webbrowser.open('qa-check.txt')


def finished():
    """The last area with help, save, test, view and quit buttons."""
    Bg.q_a_btn = Button(finished_btn_frame, bg='springgreen', text='  QA  ',
                      command=check_qa)
    Bg.q_a_btn.grid(row=8, column=0, pady=15, padx=15)

    ttips.Create(Bg.q_a_btn,
                 'Feature no yet available in this version.\n'
                 'Click here to check that your\n'
                 'answers match your questions.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)
    Bg.q_a_btn.configure(state=DISABLED)
    
    help_btn = Button(finished_btn_frame, bg='yellow', text=' Help ',
                      command=display_help_text)
    help_btn.grid(row=8, column=1, pady=15, padx=15)

    ttips.Create(help_btn,
                 'Click here to show a full help guide.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)

    Bg.save_btn = Button(finished_btn_frame,
                         bg='white',
                         text=' Save ',
                         command=save_settings)
    Bg.save_btn.grid(row=8, column=2, pady=15, padx=15)

    ttips.Create(Bg.save_btn,
                 'Save all your settings',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)

    Bg.test_btn = Button(finished_btn_frame,
                         bg='plum',
                         text=' Test ',
                         command=test_quiz)
    Bg.test_btn.grid(row=8, column=3, pady=15, padx=15)

    ttips.Create(Bg.test_btn,
                 'Run your quiz in test mode.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)

    Bg.open_folder_btn = Button(finished_btn_frame,
                                bg='lightblue',
                                text=' View ',
                                command=open_folder)
    Bg.open_folder_btn.grid(row=8, column=4, pady=15, padx=15)

    ttips.Create(Bg.open_folder_btn,
                 'Click here to view the folder containing all\n'
                 'the files your program needs to run independently.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)
    
    quit_btn = Button(finished_btn_frame, bg='orange', text=' Quit ',
                      command=quit_prg)
    quit_btn.grid(row=8, column=5, pady=15, padx=15)

    ttips.Create(quit_btn,
                 'Quit SQM.',
                 fontname='helvetica',
                 fontsize=12,
                 showtime=12)


def about_menu():
    """msgbox Info about this program."""
    messagebox.showinfo('Program Information', 'Simple Quiz Maker V0.60\n'
                        'Freeware, but (c) Steve Shambles, July 2020')


def visit_blog_menu():
    """Visit my python blog from the drop down menu."""
    webbrowser.open('https:\\stevepython.wordpress.com')


def contact_menu():
    """Contact me by email via my website from menu."""
    webbrowser.open('https:\\stevepython.wordpress.com/contact/')


def donate():
    """In the vain hope someone generous likes this program enough to
       reward my work."""
    webbrowser.open("https:\\paypal.me/photocolourizer")


def display_help_text():
    """show help text in users default text editor."""
    webbrowser.open('help.txt')

# My standard drop-down menu.
MENU_BAR = Menu(root)
FILE_MENU = Menu(MENU_BAR, tearoff=0)
MENU_BAR.add_cascade(label='Menu', menu=FILE_MENU)
FILE_MENU.add_command(label='Help', command=display_help_text)
FILE_MENU.add_command(label='About', command=about_menu)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Contact me', command=contact_menu)
FILE_MENU.add_command(label='Visit my blog', command=visit_blog_menu)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Make a small donation via PayPal', command=donate)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Exit', command=quit_prg)
root.config(menu=MENU_BAR)

# Start.
ask_quiz_name()
logo_load_btn()
Bg.logo_btn.configure(state=DISABLED)
accept_btn()
Bg.accept_logo_btn.configure(state=DISABLED)
step_3()
Bg.qf_btn.configure(state=DISABLED)
Bg.af_btn.configure(state=DISABLED)
finished()

Bg.save_btn.configure(state=DISABLED)
Bg.test_btn.configure(state=DISABLED)
Bg.open_folder_btn.configure(state=DISABLED)


load_example_logo()

root.protocol("WM_DELETE_WINDOW", quit_prg)

root.mainloop()
