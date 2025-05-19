import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os

HOST = input("Enter server address (e.g. 7.tcp.eu.ngrok.io): ").strip()
PORT = int(input("Enter server port (e.g. 17856): ").strip())

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("DOOM Eternal Chat")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        # Load Doom background
        bg_image = Image.open("doom_bg.jpg")
        bg_image = bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Load custom font or fallback
        try:
            self.custom_font = tkFont.Font(file="fonts/doom.ttf", size=12)
        except:
            self.custom_font = ("Consolas", 12)

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, bg="#2b2b2b", fg="#f04747",
                                                   insertbackground="#f04747", font=self.custom_font)
        self.chat_area.config(state='disabled', borderwidth=2, relief="groove")
        self.canvas.create_window(20, 20, anchor="nw", width=760, height=450, window=self.chat_area)

        # Message entry box
        self.msg_entry = tk.Entry(master, bg="#1a1a1a", fg="#ffffff", insertbackground="#ffffff", font=self.custom_font)
        self.canvas.create_window(20, 490, anchor="nw", width=600, height=30, window=self.msg_entry)
        self.msg_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(
            master,
            text="SEND",
            bg="#8B0000",
            fg="white",
            activebackground="#B22222",
            activeforeground="white",
            font=self.custom_font,
            command=self.send_message
        )
        self.canvas.create_window(640, 490, anchor="nw", width=140, height=30, window=self.send_button)

        # Connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = simpledialog.askstring("Username", "Enter your username", parent=master)
        if not self.username:
            master.destroy()
            return

        try:
            self.client_socket.connect((HOST, PORT))
            self.client_socket.send(self.username.encode())
        except:
            self.display_message("❌ Connection failed.")
            return

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        message = self.msg_entry.get()
        self.msg_entry.delete(0, tk.END)
        if message:
            try:
                self.client_socket.send(message.encode())
            except:
                self.display_message("❌ Message failed to send.")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                self.display_message(message)
            except:
                break

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
