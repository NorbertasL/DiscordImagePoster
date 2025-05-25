# gui.py
import tkinter as tk
from tkinter import ttk
from db import init_db, get_webhooks, add_webhook


def main_config_gui():
    init_db()
    root = tk.Tk()
    root.title("Screenshot Config")
    root.geometry("600x400")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # --- Webhook Manager Tab ---
    webhook_frame = ttk.Frame(notebook)
    notebook.add(webhook_frame, text='WebHook Manager')

    # Webhook form
    ttk.Label(webhook_frame, text="Title").grid(row=0, column=0)
    title_entry = ttk.Entry(webhook_frame)
    title_entry.grid(row=0, column=1)

    ttk.Label(webhook_frame, text="Webhook URL").grid(row=1, column=0)
    url_entry = ttk.Entry(webhook_frame)
    url_entry.grid(row=1, column=1)

    ttk.Label(webhook_frame, text="Description").grid(row=2, column=0)
    desc_entry = ttk.Entry(webhook_frame)
    desc_entry.grid(row=2, column=1)

    def save_webhook():
        add_webhook(title_entry.get(), url_entry.get(), desc_entry.get())
        title_entry.delete(0, 'end')
        url_entry.delete(0, 'end')
        desc_entry.delete(0, 'end')
        refresh_webhooks()

    ttk.Button(webhook_frame, text="Add Webhook", command=save_webhook).grid(row=3, column=1, sticky='e')

    # Webhook List
    webhook_listbox = tk.Listbox(webhook_frame, width=80)
    webhook_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def refresh_webhooks():
        webhook_listbox.delete(0, 'end')
        for id, title, url, desc in get_webhooks():
            webhook_listbox.insert('end', f"{title} - {url} - {desc}")

    refresh_webhooks()

    # Placeholder for + tab (future dynamic tabs)
    plus_frame = ttk.Frame(notebook)
    notebook.add(plus_frame, text='+')

    root.mainloop()
