from tkinter import *
from tkinter import messagebox


def check_is_line():
    global tabla
    check_mutari = [[-1, 1], [-3, 3], [-4, 4], [-2, 2]]
    for i in range(9):
        if i == 1 or i == 7:
            if tabla[i]['text'] == tabla[i + check_mutari[0][0]]['text'] == tabla[i + check_mutari[0][1]]['text']:
                if tabla[i]['text'] != ' ':
                    return tabla[i]['text']
        elif i == 3 or i == 5:
            if tabla[i]['text'] == tabla[i + check_mutari[1][0]]['text'] == tabla[i + check_mutari[1][1]]['text']:
                if tabla[i]['text'] != ' ':
                    return tabla[i]['text']
        elif i == 4:
            for j in range(len(check_mutari)):
                if tabla[i]['text'] == tabla[i + check_mutari[j][0]]['text'] == tabla[i + check_mutari[j][1]]['text']:
                    if tabla[i]['text'] != ' ':
                        return tabla[i]['text']
    return 0


def disable_buttons():
    global tabla
    for i in range(len(tabla)):
        tabla[i].config(state=DISABLED)


def return_gol(mutari, i):
    global tabla
    if tabla[i]['text'] == tabla[i + mutari[0]]['text'] and tabla[i + mutari[1]]['text'] == ' ':
        if tabla[i]['text'] != ' ':
            return [i + mutari[1], tabla[i]['text']]
    elif tabla[i]['text'] == tabla[i + mutari[1]]['text'] and tabla[i + mutari[0]]['text'] == ' ':
        if tabla[i]['text'] != ' ':
            return [i + mutari[0], tabla[i]['text']]
    elif tabla[i + mutari[1]]['text'] == tabla[i + mutari[0]]['text'] and tabla[i]['text'] == ' ':
        if tabla[i + mutari[1]]['text'] != ' ':
            return [i, tabla[i + mutari[1]]['text']]
    return [-1, -1]


def is_gol():
    check_mutari = [[-1, 1], [-3, 3], [-4, 4], [-2, 2]]
    next_poz = -1
    for i in range(9):
        if i == 1 or i == 7:
            poz = return_gol(check_mutari[0], i)
            if poz[0] != -1:
                next_poz = poz[0]
                if poz[1] == '0':
                    return next_poz
        elif i == 3 or i == 5:
            poz = return_gol(check_mutari[1], i)
            if poz[0] != -1:
                next_poz = poz[0]
                if poz[1] == 'O':
                    return next_poz
        elif i == 4:
            for j in range(len(check_mutari)):
                poz = return_gol(check_mutari[j], i)
                if poz[0] != -1:
                    next_poz = poz[0]
                    if poz[1] == 'O':
                        return next_poz
    return next_poz


def check_win():
    global win
    castigator = check_is_line()
    if castigator:
        messagebox.showinfo('Tic Tac Toe', f'{castigator} won the match')
        disable_buttons()
        win = True
    elif count == 9:
        messagebox.showinfo('Tic Tac Toe', 'Nobody won')
        disable_buttons()
        win = True


def robot_move():
    global count, index_robot
    mutari_robot = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    count += 1
    next_poz = is_gol()
    if next_poz != -1:
        tabla[next_poz]['text'] = 'O'
    else:
        while tabla[mutari_robot[index_robot] - 1]['text'] != ' ' and index_robot < 8:
            index_robot += 1
        tabla[mutari_robot[index_robot] - 1]['text'] = 'O'


def player_move(b):
    global count
    if clicked is True:
        b['text'] = 'X'
    else:
        b['text'] = 'O'
    count += 1


def b_click(b):
    global clicked, rand
    if b['text'] == ' ':
        if singur is False:
            player_move(b)
            check_win()
            clicked = not clicked
        else:
            player_move(b)
            check_win()
            if win is False:
                robot_move()
                check_win()
    else:
        messagebox.showerror('Tic Tac Toe', 'That box has already selected\nPlease pick another box')


def reset(window, multiplayer):
    global count, clicked, tabla, index_robot, win, singur, rand
    index_robot = count = 0
    win = False
    singur = multiplayer
    if singur is False:
        clicked = rand
    else:
        clicked = True
    rand = not rand
    b1 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b1))
    b2 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b2))
    b3 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b3))

    b4 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b4))
    b5 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b5))
    b6 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b6))

    b7 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b7))
    b8 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b8))
    b9 = Button(window, text=' ', font=('Helvetica', 20), height=3, width=10, bg='white', command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    tabla = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    my_menu = Menu(window)
    window.config(menu=my_menu)
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label='Options', menu=options_menu)
    options_menu.add_command(label='Reset Game', command=lambda: reset(window, multiplayer))
    options_menu.add_command(label='Play vs Robot', command=lambda: reset(window, True))
    options_menu.add_command(label='Play vs Someone', command=lambda: reset(window, False))
    options_menu.add_command(label='Quit Game', command=window.destroy)


def start_menu(window):
    single_player = Button(window, text='Single Player', font=('Helvetica', 20), height=3, width=10, bg='white',
                           command=lambda: reset(window, True))
    two_player = Button(window, text='Two Players', font=('Helvetica', 20), height=3, width=10, bg='white',
                        command=lambda: reset(window, False))
    single_player.grid(row=0, column=0)
    two_player.grid(row=1, column=0)


def main_menu(window):
    start = Button(window, text='Start Game', font=('Helvetica', 20), height=3, width=10, bg='white',
                   command=lambda: start_menu(window))
    quit = Button(window, text='Quit Game', font=('Helvetica', 20), height=3, width=10, bg='white',
                  command=window.destroy)
    start.grid(row=0, column=0)
    quit.grid(row=1, column=0)


def main():
    global rand
    rand = True
    window = Tk()
    window.title('Tic Tac Toe')
    main_menu(window)
    window.mainloop()


main()
