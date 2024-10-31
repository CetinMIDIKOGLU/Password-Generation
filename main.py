from tkinter import*
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    #password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&','*', '+','.']

    password_entry.delete(0,END)
    password_letters = [choice(letters) for _ in range(randint(7,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_nubers = [choice(numbers) for _ in range(randint(2,4))]
    
    password_list = password_letters + password_symbols + password_nubers
    shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=website_entry.get().upper()
    email=email_entry.get().lower()
    password=password_entry.get()
    new_data={
        website:{
            "email": email,
            "password": password,
        }
    }
    
    if website=="" or password=="" or email=="" :
        messagebox.showinfo(title=website,message=f"Boşlukları doldurduğunuza emin olun.")
        
    else:
        try:
            
            with open("not.json",mode="r") as file:  
                data= json.load(file)
                try:
                    old_password = data[website]["password"]
                except KeyError:
                    pass
                
        except FileNotFoundError:
            with open("not.json",mode="w") as file:
                json.dump(new_data,file,indent=4)
                
                
        else:
            if website in data:
                choice=messagebox.askokcancel(title=website,message=f"{website} İçin kayıt bulunuyor şifreyi güncelemek ister misiniz?\nEski şifre: {old_password}\nYeni şifre: {password}")
                if choice==True:
                    data.update(new_data)
                    with open("not.json",mode="w") as file:
                        json.dump(data,file,indent=4)
                else:
                    pass
                
            else: 
                data.update(new_data)
                with open("not.json",mode="w") as file:
                    json.dump(data,file,indent=4)
                
                           
        
        
def search():
    website=website_entry.get().upper()
    try:
        with open("not.json",mode="r") as file:  
            data=json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="ERROR",message=f"Daha önce hiç not girilmedi.")
        
    else:        
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
           
        
        else:
            messagebox.showinfo(title="ERROR",message=f"{website} ile ilgili not bulunmuyor.")
    
                
def email():
    try:
        with open("not.json",mode="r") as file:  
                data=json.load(file) 
            
        last_key = list(data.keys())[-1]
        last_item = data[last_key]
        last_email = last_item["email"]
        
    except FileNotFoundError:
       last_email="example@gmail.com"
       
    finally:
        email_entry.insert(0,last_email)        


# ---------------------------- UI SETUP ------------------------------- #
BG="#2F3645"
BUTTONCOLOR="#31363F" 
FG="#EEEDEB"
ENTRYCOLOR="#B6BBC4"
coor="x"
window =Tk()
window.title("Passwords Manager")
window.config(padx=50,pady=50,bg=BG)


canvas=Canvas(width=200, height=200,highlightthickness=0,bg=BG)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(75, 90, image=logo_img)
canvas.grid(column=1,row=0)

#Labels
website_label=Label(text="Website:",bg=BG,font=("Courier",20,"bold"),fg=FG)
website_label.grid(column=0,row=1,padx=2)

email_label=Label(text="Email/Username:",bg=BG,font=("Courier",20,"bold"),fg=FG)
email_label.grid(column=0,row=2,padx=2)

password_label=Label(text="Password:",bg=BG,font=("Courier",20,"bold"),fg=FG)
password_label.grid(column=0,row=3,padx=2)

#Entrys
website_entry=Entry(width=31,bg=ENTRYCOLOR)
website_entry.grid(column=1,row=1, sticky="E",pady=5)

email_entry=Entry(width=51,bg=ENTRYCOLOR)
email_entry.grid(column=1,row=2,columnspan=2,pady=5)


password_entry=Entry(width=31,bg=ENTRYCOLOR)
password_entry.grid(column=1,row=3, sticky="E",pady=5)


#Buttons
generate_button=Button(text="Generate Password",command=gen_password,bg=BUTTONCOLOR,fg=FG)
generate_button.grid(column=2,row=3, sticky="W",padx=10)

add_buton=Button(text="Add",width=43,command=save_password,bg=BUTTONCOLOR,fg=FG)
add_buton.grid(column=1,row=4,columnspan=3,pady=5)

search_button=Button(text="Search",command=search,bg=BUTTONCOLOR,fg=FG,width=15)
search_button.grid(column=2,row=1, sticky="W",padx=10)
                     

email()


window.mainloop()