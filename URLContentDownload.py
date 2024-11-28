import requests
import tkinter as tk
from tkinter import filedialog, messagebox

def download_content():
    url = url_entry.get()
    filename = filedialog.asksaveasfilename(
        defaultextension="",
        filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Images", "*.jpg *.png"), ("HTML Files", "*.html")]
    )
    
    if not url or not filename:
        messagebox.showwarning("Warning", "URL or filename cannot be empty!")
        return
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            messagebox.showinfo("Success", f"Content saved successfully to {filename}")
        else:
            messagebox.showerror("Error", f"Failed to retrieve content. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI
app = tk.Tk()
app.title("Professional URL Content Downloader")

# Set background color and size
app.configure(bg="#2E4053")
app.geometry("500x250")

# Title Label
title_label = tk.Label(
    app,
    text="URL Content Downloader",
    font=("Arial", 18, "bold"),
    fg="#F7DC6F",
    bg="#2E4053"
)
title_label.pack(pady=10)

# URL Entry Section
url_label = tk.Label(
    app,
    text="Enter the URL:",
    font=("Arial", 12),
    fg="white",
    bg="#2E4053"
)
url_label.pack(pady=5)

url_entry = tk.Entry(app, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(
    app,
    text="Download Content",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#28B463",
    activebackground="#239B56",
    activeforeground="white",
    command=download_content
)
download_button.pack(pady=20)

# Run the GUI event loop
app.mainloop()
