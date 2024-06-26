import tkinter as tk
from time import strftime

# Function to update the time displayed on the label
def update_time():
    current_time = strftime("Time: %H:%M:%S %p")
    current_date = strftime("Date: %m/%d/%Y")
    time_label.config(text=current_time + "\n" + current_date)
    time_label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label for displaying time and date
time_label = tk.Label(root, font=('Helvetica', 50, 'bold'), background='lightblue', foreground='navy')
time_label.pack(anchor='center',pady=20)

# Call the update_time function initially to display the current time
update_time()

# Run the Tkinter event loop
root.mainloop()
