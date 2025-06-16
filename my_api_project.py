import tkinter as tk
from tkinter import ttk
from PIL  import Image, ImageTk
import requests
from io import BytesIO

# API থেকে ইউজার ডেটা আনা
def get_random_user():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]

        name = user['name']
        location = user['location']
        email = user['email']
        phone = user['phone']
        picture_url = user['picture']['large']

        # GUI তে তথ্য আপডেট করা
        name_label.config(text=f"{name['title']} {name['first']} {name['last']}")
        location_label.config(text=f"{location['city']}, {location['country']}")
        email_label.config(text=email)
        phone_label.config(text=phone)

        # ছবি লোড করা
        img_response = requests.get(picture_url)
        img_data = Image.open(BytesIO(img_response.content))
        img_data = img_data.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img_data)
        photo_label.config(image=img_tk)
        photo_label.image = img_tk
    else:
        name_label.config(text="Failed to fetch data")

# GUI Window তৈরি
root = tk.Tk()
root.title("Random User Generator")
root.geometry("300x400")
root.configure(padx=10, pady=10)

# Image Placeholder
photo_label = tk.Label(root)
photo_label.pack(pady=10)

# Labels
name_label = ttk.Label(root, text="Name", font=("Arial", 12, "bold"))
name_label.pack(pady=5)

location_label = ttk.Label(root, text="Location", font=("Arial", 10))
location_label.pack(pady=5)

email_label = ttk.Label(root, text="Email", font=("Arial", 10))
email_label.pack(pady=5)

phone_label = ttk.Label(root, text="Phone", font=("Arial", 10))
phone_label.pack(pady=5)

# Button
generate_button = ttk.Button(root, text="Generate New User", command=get_random_user)
generate_button.pack(pady=20)

# Run first fetch
get_random_user()

# Run the GUI loop
root.mainloop()
