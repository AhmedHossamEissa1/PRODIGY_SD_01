import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Create the main application window
app = tk.Tk()
app.title("Temperature Converter")

# Set the window size and disable resizing
app.geometry("800x600")
app.resizable(False, False)

# Load background image
background_image = Image.open("photo.jpg")
# Resize the image to fit the window size
background_image = background_image.resize((800, 600))
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label and entry for input
input_label = tk.Label(app, text="Enter temperature:", font=("Arial", 16))
input_label.place(relx=0.5, rely=0.4, anchor="center")

input_entry = tk.Entry(app, font=("Arial", 14))
input_entry.place(relx=0.5, rely=0.45, anchor="center")

# Create a space between the "Enter temperature" label and the "Select unit" label
space_label = tk.Label(app, text="", font=("Arial", 16))
space_label.place(relx=0.5, rely=0.5, anchor="center")

# Create a ComboBox for selecting temperature units
unit_label = tk.Label(app, text="Select unit:", font=("Arial", 16))
unit_label.place(relx=0.5, rely=0.55, anchor="center")

unit_var = tk.StringVar()
unit_combo = ttk.Combobox(app, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 14))
unit_combo.place(relx=0.5, rely=0.6, anchor="center")
unit_combo.current(0)  # Set default selection to Celsius

# Create a function to handle button click event
def process_input():
    user_input = input_entry.get()
    selected_unit = unit_var.get()

    if not user_input:
        output_label.config(text="Please enter a temperature!", font=("Arial", 14))
        return

    user_input = float(user_input)

    if selected_unit == "Celsius":
        fahrenheit = user_input * 9/5 + 32
        kelvin = user_input + 273.15
        output_label.config(text=f"Fahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K", font=("Arial", 14))
    elif selected_unit == "Fahrenheit":
        celsius = (user_input - 32) * 5/9
        kelvin = (user_input - 32) * 5/9 + 273.15
        output_label.config(text=f"Celsius: {celsius:.2f} °C\nKelvin: {kelvin:.2f} K", font=("Arial", 14))
    elif selected_unit == "Kelvin":
        celsius = user_input - 273.15
        fahrenheit = (user_input - 273.15) * 9/5 + 32
        output_label.config(text=f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F", font=("Arial", 14))

# Create a button to process input
process_button = tk.Button(app, text="Convert", command=process_input, font=("Arial", 14))
process_button.place(relx=0.5, rely=0.65, anchor="center")

# Create a label to display the output
output_label = tk.Label(app, text="", justify="center", font=("Arial", 16))
output_label.place(relx=0.5, rely=0.75, anchor="center")

# Start the main event loop
app.mainloop()
