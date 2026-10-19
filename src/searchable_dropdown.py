
import tkinter as tk
import customtkinter as ctk


class SearchableDropdown(ctk.CTkFrame):
    def __init__(
        self,
        master,
        values,
        height=42,
        visible_items=5,
        font=("Inter", 14),
        dropdown_font=("Arial", 22),
        fg_color="#E9F2F1",
        button_color="#E9F2F1",
        button_hover_color="#D8E8E6",
        text_color="#167D78",
        dropdown_text_color="#263238",
        **kwargs
    ):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.values = list(values)
        self.visible_items = max(1, visible_items)
        self.font = font
        self.dropdown_font = dropdown_font
        self.fg_color = fg_color
        self.button_hover_color = button_hover_color
        self.text_color = text_color
        self.dropdown_text_color = dropdown_text_color
        self.selected_value = self.values[0] if self.values else ""
        self.search_entry = ctk.CTkEntry(
            self,
            height=height,
            placeholder_text="Search currency code or name..",
            font=self.font
        )
        self.search_entry.pack(fill="x", pady=(0, 6))
        self.search_entry.bind("<KeyRelease>", self.filter_options)
        self.dropdown_button = ctk.CTkButton(
            self,
            text=self.selected_value,
            height=height,
            anchor="w",
            font=self.font,
            fg_color=button_color,
            hover_color=self.button_hover_color,
            text_color=self.text_color,
            command=self.toggle_popup
        )
        self.dropdown_button.pack(fill="x")
        self.popup = tk.Toplevel(self)
        self.popup.withdraw()
        self.popup.overrideredirect(True)
        self.popup.resizable(False, False)
        self.listbox = tk.Listbox(
            self.popup,
            height=self.visible_items,
            width=1,
            font=self.dropdown_font,
            bg="#FFFFFF",
            fg=self.dropdown_text_color,
            selectbackground=self.fg_color,
            selectforeground=self.text_color,
            activestyle="none",
            highlightthickness=0,
            relief="flat",
            borderwidth=0
        )
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(
            self.popup,
            orient="vertical",
            command=self.listbox.yview
        )
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.configure(yscrollcommand=self.scrollbar.set)

        self.listbox.bind("<ButtonRelease-1>", self.select_option)
        self.listbox.bind("<Return>", self.select_option)
        self.popup.bind("<FocusOut>", self.on_popup_focus_out)

    def show_popup(self, options):
        self.listbox.delete(0, tk.END)

        for option in options:
            self.listbox.insert(tk.END, option)

        if not options:
            self.listbox.insert(tk.END, "Currency not found")

        self.update_idletasks()
        x = self.search_entry.winfo_rootx()
        y = (
            self.search_entry.winfo_rooty()
            + self.search_entry.winfo_height()
        )
        width = self.search_entry.winfo_width()
        visible_count = min(
            max(len(options), 1),
            self.visible_items
        )
        row_height = 40
        popup_height = visible_count * row_height + 4
        self.popup.geometry(
            f"{width}x{popup_height}+{x}+{y}"
        )
        self.popup.update_idletasks()
        self.popup.deiconify()
        self.popup.lift()

    def toggle_popup(self):
        if self.popup.state() != "withdrawn":
            self.close_popup()
        else:
            self.show_popup(self.values)

    def filter_options(self, event=None):
        query = self.search_entry.get().strip().lower()

        if not query:
            self.close_popup()
            return

        filtered = [
            value
            for value in self.values
            if query in value.lower()
        ]

        self.show_popup(filtered)

    def select_option(self, event=None):
        selection = self.listbox.curselection()

        if not selection:
            return

        value = self.listbox.get(selection[0])

        if value not in self.values:
            return

        self.selected_value = value
        self.dropdown_button.configure(text=value)
        self.search_entry.delete(0, tk.END)
        self.close_popup()

    def on_popup_focus_out(self, event=None):
        self.close_popup()

    def close_popup(self):
        if self.popup.winfo_exists():
            self.popup.withdraw()

    def get(self):
        return self.selected_value

    def set(self, value):
        if value in self.values:
            self.selected_value = value
            self.dropdown_button.configure(text=value)
            self.search_entry.delete(0, tk.END)
            self.close_popup()
