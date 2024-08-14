import requests
import tkinter as tk


def generate_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)


# -------- UI --------#

window = tk.Tk()
window.config(bg='white', padx=50, pady=50)
quote_img = tk.PhotoImage(file='background.png')
canvas = tk.Canvas(window, bg='white', height=414, width=300, highlightthickness=0)
canvas.create_image(150, 207, image=quote_img)
quote_text = canvas.create_text(150, 207, text='', fill='black', font='Helvetica 16 bold italic', width=250)
canvas.grid(column=0, row=0)

kanye_img = tk.PhotoImage(file='kanye.png')
button = tk.Button(image=kanye_img, command=generate_quote, borderwidth=0, highlightthickness=0)
button.grid(column=0, row=1)

window.mainloop()