# Simple login screen written using the PySimpleGui library
#

import PySimpleGUI as sg

# Layout of the login screen
layout = [
    [sg.Text("Username:"), sg.Input(key="key_username")],
    [sg.Text("Password:"), sg.Input(key="key_password", password_char="*")],
    [sg.Button("Log In", key="event_login")]
]

# Create window
window = sg.Window("Log In", layout)

# Event loop
while True:
    event, values = window.read()
    print(event)
    if event == sg.WINDOW_CLOSED:
        break

    elif event == "event_login":
        print("Log on button clicked")

        # Get username and password
        username = values["key_username"]
        password = values["key_password"]

        # Do something sensible with them here

        # Clear the widgets
        window["key_username"].update("")
        window["key_userpassword"].update("")

        sg.popup("Logged in successfully!")

    else:
        print("Some other event that I haven't thought about: ", event)

    

# Close window
window.close()
