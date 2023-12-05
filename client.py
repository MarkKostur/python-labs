import socket
import tkinter as tk
from functools import partial
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message_to_chat(entry, chat_frame):
    text = entry.get()
    if text.lower() == "quit":
        client.close()
        root.destroy()
        return
    client.send(text.encode())

    add_message_to_chat(chat_frame, f"You: {text}")

def receive_messages(chat_frame):
    client.connect(("localhost", 12345))
    print('client', client)

    while True:
        message = client.recv(1024).decode()
        if not message:
            break

        add_message_to_chat(chat_frame, f"Server: {message}")

def add_message_to_chat(chat_frame, message):
    chat_frame.insert(tk.END, f"{message}\n")
    chat_frame.see(tk.END)

def create_chat():
    container_messages = tk.Frame(root, borderwidth=2, relief="solid")
    container_messages.grid(row=0, column=0, sticky="nsew", padx=60, pady=60)
    root.grid_rowconfigure(0, weight=8)
    root.grid_columnconfigure(0, weight=1)

    chat_frame = tk.Text(container_messages, background='#FFFFFF', foreground='black', height=20, width=60, state='normal')
    chat_frame.pack(fill='both', expand=True)

    container_input_and_btn = tk.Frame(root, borderwidth=2, relief="solid")
    container_input_and_btn.grid(row=1, column=0, sticky="nsew", padx=20, pady=container_input_and_btn.winfo_reqheight()//2)
    root.grid_rowconfigure(1, weight=2)

    entry_button_container = tk.Frame(container_input_and_btn, borderwidth=2, relief='solid')
    entry_button_container.pack(side="top", pady=5)

    entry = tk.Entry(entry_button_container, foreground="black", justify='center')
    button_send = tk.Button(entry_button_container, text="Send message", width=15, background='#2AABEE', foreground='white', justify='center', command=partial(send_message_to_chat, entry=entry, chat_frame=chat_frame))

    entry.insert(0, "Type your message...")
    entry.pack(side="left", padx=(0, 5))
    button_send.pack(side="left")

    return chat_frame

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('1280x720')
    root.title('Chat')

    chat_frame = create_chat()

    receive_thread = Thread(target=receive_messages, args=(chat_frame,), daemon=True)
    receive_thread.start()

    root.mainloop()
