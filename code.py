import tkinter as tk
import keyboard
import time

code_list = 'codes.txt'
usedcode_file = 'used_codes.txt'

with open(code_list, 'r') as file:
    top_rust_codes = file.read().splitlines()

used_codes = set()

try:
    with open(usedcode_file, 'r') as savefile:
        used_codes.update(savefile.read().splitlines())
except FileNotFoundError:
    pass

next_code_index = 0
cooldown_active = False

def save_progress():
    with open(usedcode_file, 'w') as savefile:
        savefile.write('\n'.join(used_codes))

def enter_code(rust_code):
    for code in rust_code:
        keyboard.send(code)
        time.sleep(0.1)
        entered_code_label.config(text=f"Tried Combs: {len(used_codes)}")

def generate_next_code():
    global next_code_index, cooldown_active
    if not cooldown_active:
        while next_code_index < len(top_rust_codes):
            rust_code = top_rust_codes[next_code_index]
            if rust_code not in used_codes:
                used_codes.add(rust_code)
                save_progress()
                next_code_index += 1
                result_label.config(text=f"Current Code: {rust_code}")
                enter_code(rust_code)
                cooldown_active = True
                root.after(2000, reset_cooldown)  
                return
            else:
                next_code_index += 1

        result_label.config(text="All Codes tested.")

def reset_cooldown():
    global cooldown_active
    cooldown_active = False

root = tk.Tk()
root.title("CodeHacker")

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

entered_code = []
entered_code_label = tk.Label(root, text="Tried Combs: ", font=("Arial", 12))
entered_code_label.pack()

# Hotkey F2
keyboard.add_hotkey('F2', generate_next_code)

root.mainloop()
