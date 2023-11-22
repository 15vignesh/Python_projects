import tkinter as tk

# Dictionary mapping characters to Morse Code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
    ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': '/'
}


def translate_to_morse():
    text = input_text.get("1.0", tk.END).upper().strip()
    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, morse_code)


def translate_to_text():
    morse_code = input_text.get("1.0", tk.END).strip().split(" ")
    text = ""
    for code in morse_code:
        for char, morse in morse_code_dict.items():
            if morse == code:
                text += char
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text)


# Create the main window
window = tk.Tk()
window.title("Morse Code Translator")

# Create the input text box
input_label = tk.Label(window, text="Input:")
input_label.pack(pady=10)
input_text = tk.Text(window, height=5, width=50)
input_text.pack()

# Create the translate buttons
translate_frame = tk.Frame(window)
translate_frame.pack(pady=10)
to_morse_button = tk.Button(translate_frame, text="Translate to Morse Code", command=translate_to_morse)
to_morse_button.grid(row=0, column=0, padx=5)
to_text_button = tk.Button(translate_frame, text="Translate to Text", command=translate_to_text)
to_text_button.grid(row=0, column=1, padx=5)

# Create the output text box
output_label = tk.Label(window, text="Output:")
output_label.pack(pady=10)
output_text = tk.Text(window, height=5, width=50)
output_text.pack()
window.mainloop()
