import tkinter as tk
from tkinter import messagebox

motor_labels = [
    "Index",
    "Middle",
    "Ring",
    "Pinkie",
    "Thumb",
    "Thumb - Stretch",
    "Wrist Motor"
]

# Clear data.txt on launch
try:
    with open("data.txt", "w") as file:
        file.write("")
except Exception as e:
    print(f"Warning: Could not clear data.txt: {e}")

# Create main window
root = tk.Tk()
root.title("Prosthetic Arm Preset Creator")

# Preset Name Entry
tk.Label(root, text="Preset Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
preset_name_entry = tk.Entry(root, width=30)
preset_name_entry.grid(row=0, column=1, padx=5, pady=5)

# Action Finger Instructions Label
tk.Label(root, text="Select Action Fingers:").grid(row=0, column=2, columnspan=2, padx=5, pady=(0, 5), sticky="w")

entries = {}
check_vars = {}

def toggle_entry(label):
    """Enables/disables entry based on checkbox state."""
    if check_vars[label].get() == 1:
        entries[label].config(state='disabled')
    else:
        entries[label].config(state='normal')

# Create motor entry fields with checkboxes
start_row = 2
for i, label_text in enumerate(motor_labels):
    tk.Label(root, text=label_text + ":").grid(row=start_row + i, column=0, padx=5, pady=3, sticky="e")
    
    entry = tk.Entry(root, width=30)
    entry.grid(row=start_row + i, column=1, padx=5, pady=3)
    entries[label_text] = entry

    var = tk.IntVar()
    check = tk.Checkbutton(root, variable=var, command=lambda l=label_text: toggle_entry(l))
    check.grid(row=start_row + i, column=2, padx=5, pady=3)
    check_vars[label_text] = var

def save_preset():
    preset_name = preset_name_entry.get().strip()
    if not preset_name:
        messagebox.showerror("Input Error", "Please enter a preset name.")
        return

    motor_values = []
    for label_text in motor_labels:
        if check_vars[label_text].get() == 1:
            motor_values.append("181")  # If checkbox is checked, set to 181
        else:
            value_str = entries[label_text].get().strip()
            try:
                value_int = int(value_str)
            except ValueError:
                messagebox.showerror("Input Error", f"Please enter a valid integer for '{label_text}'.")
                return
            if value_int < 0 or value_int > 180:
                messagebox.showerror("Input Error", f"Value for '{label_text}' must be between 0 and 180.")
                return
            motor_values.append(value_int)

    preset_line = preset_name + "," + ",".join(map(str, motor_values)) + "\n"

    try:
        with open("data.txt", "a") as file:
            file.write(preset_line)
        messagebox.showinfo("Success", "Preset saved successfully!")
    except Exception as e:
        messagebox.showerror("File Error", f"An error occurred while writing the file:\n{e}")

    preset_name_entry.delete(0, tk.END)
    for label_text in motor_labels:
        entries[label_text].config(state='normal')
        entries[label_text].delete(0, tk.END)
        check_vars[label_text].set(0)

# Save Button
save_button = tk.Button(root, text="Save Preset", command=save_preset)
save_button.grid(row=start_row + len(motor_labels), column=0, columnspan=3, pady=10)

# Start main loop
root.mainloop()
