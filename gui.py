"""Provides a Graphical User Interface for configuring the webhook2discord bot."""
import tkinter as tk
from tkinter import ttk
from db import init_db, get_webhooks, add_webhook

def main_config_gui():
    """
    Initializes the main configuration window and starts the main event loop.
    This is the entry point for the GUI.
    """
    init_db()

    root = tk.Tk()
    main_frame = ttk.Notebook(root)
    main_frame.pack(expand=True, fill='both')

    webhook_tab = WebhookManagerTab(main_frame)
    main_frame.add(webhook_tab.frame, text='WebHook Manager')

    # Placeholder for + tab (future dynamic tabs)
    event_tab = EventsTab(main_frame)
    main_frame.add(event_tab.frame, text='Events')

    root.mainloop()

class WebhookManagerTab:
    """
    A tab in the main configuration window that allows users to create and
    manage webhooks.
    """
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self._build_ui()

    def _build_ui(self):
        ttk.Label(self.frame, text="Title").grid(row=0, column=0)
        self.title_entry = ttk.Entry(self.frame)
        self.title_entry.grid(row=0, column=1)

        ttk.Label(self.frame, text="Webhook URL").grid(row=1, column=0)
        self.url_entry = ttk.Entry(self.frame)
        self.url_entry.grid(row=1, column=1)

        ttk.Label(self.frame, text="Description").grid(row=2, column=0)
        self.desc_entry = ttk.Entry(self.frame)
        self.desc_entry.grid(row=2, column=1)

        ttk.Button(self.frame, text="Add Webhook",
                   command=self._save_webhook).grid(row=3, column=1, sticky='e')

        self.webhook_listbox = tk.Listbox(self.frame, width=80)
        self.webhook_listbox.grid(row=4, column=0, columnspan=2, pady=10)

        self._refresh_webhooks()

    def _save_webhook(self):
        add_webhook(
            self.title_entry.get(),
            self.url_entry.get(),
            self.desc_entry.get()
        )

        # Clear fields
        self.title_entry.delete(0, 'end')
        self.url_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')
        self._refresh_webhooks()

    def _refresh_webhooks(self):
        self.webhook_listbox.delete(0, 'end')
        for _id, title, url, desc in get_webhooks():
            self.webhook_listbox.insert('end', f"{title} - {url} - {desc}")

class EventsTab:
    """
    Tab for managing events.

    The EventsTab will be responsible for displaying existing events, allowing
    the user to add new events, and allowing the user to remove events.
    """
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(expand=True, fill='both')

        self._add_placeholder_tab()
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

    def _add_placeholder_tab(self):
        self.plus_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.plus_tab, text='+')

    def _on_tab_changed(self, event):
        selected_index = self.notebook.index(self.notebook.select())
        selected_tab_text = self.notebook.tab(selected_index, "text")
        if selected_tab_text == '+':
            # In the future this will create a new event tab
            pass
