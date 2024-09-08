import platform
import subprocess
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Thesis Template')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.output = tk.Text(self, wrap='word', bg='#222', fg='#eee')
        self.output.insert(tk.END, 'Thesis Template\n===\n')
        self.output.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        frame = tk.Frame(self)
        frame.grid(row=1, column=0, columnspan=2,padx=5, pady=5, sticky='ew')
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)

        self.input = tk.Text(frame, height=2, bg='#222', fg='#eee', insertbackground='#eee')
        self.input.grid(row=1, column=0, sticky='ew')
        self.input.bind('<KeyPress>', self.on_key_press)

        self.button = tk.Button(frame, text='\u2191', command=self.on_button_click)
        self.button.grid(row=1, column=1, padx=5, sticky='ew')

        self.check()

    def on_key_press(self, event):
        if event.keysym == 'Return':
            self.send_text()
            return 'break'

    def on_button_click(self):
        self.send_text()

    def clear_text(self):
        self.input.delete('1.0', tk.END)

    def send_text(self):
        content = self.input.get('1.0', tk.END).strip()
        self.clear_text()
        self.say('> ' + content)

    def say(self, text):
        self.output.insert(tk.END, text + '\n')
        self.output.yview_moveto(1.0)

    def run(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {e}"

    def check(self):
        self.platform = platform.system()
        self.say('>> ' + self.platform)

        self.pandoc = self.run('pandoc -v')
        self.say('>> ' + self.pandoc)

if __name__ == '__main__':
    app = App()
    app.mainloop()
