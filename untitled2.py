from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Endless Dice game")
root.geometry("600x400")

root.configure(background="yellow2")

Pikachu = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
Charmender = ImageTk.PhotoImage(Image.open ("charmender.jpg"))
Bulbasour = ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
Abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
Meowth = ImageTk.PhotoImage(Image.open ("meowth.jpg"))


player1 = Label(root, text = "Player1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player1_Score_label = Label(root, bg = "royal blue", fg = "white")
player1_Score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2_Score_label = Label(root, bg = "royal blue", fg = "white")
player2_Score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

pokemon_list = [Pikachu,Charmender,Bulbasour,Abra,Iyvasour,Meowth]
power_list = [200,50,60,70,100,40]
label = Label(root)
label.place(relx = 0.5,rely = 0.5, anchor = CENTER)

player1_Score = 0
def player1():
    global player1_Score
    random_no = random.randint(0,5)
    random_pokemon = pokemon_list[random_no]
    label["image"] = random_pokemon
    
    random_power_list1 = power_list[random_no]
    player1_score = player1_score + random_power_list
    player1_Score_label["text"] = str(player1_Score)
player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player2_score = 0
def player2():
    global player2_Score
    random_no2 = random.randint(0,10)
    random_pokemon2 = pokemon_list[random_no2]
    label["image"] = random_pokemon2
    
    random_power_list2 = power_list[random_no2]
    player2_score = player2_score + random_power_list2
    player2_Score_label["text"] = str(player2_Score)
player_2_btn = Button(root, image = img, command = player2)
player_2_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)
    
    






root.mainloop()