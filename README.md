Does what it says on the tin

# Flask QR Code Generator

A simple Flask web app to generate QR codes from user-submitted URLs. This project is based on a YouTube tutorial and demonstrates basic Flask usage, form handling, and QR code generation.

## Features

- Input a URL to generate a QR code
- QR code appears only after form submission
- Prevents form resubmission on page refresh using POST-Redirect-GET pattern
- Uses Flask sessions and environment variables for security


## Notes

This project started from a tutorial by [this guy](https://www.youtube.com/watch?v=Qh6jqlfCClM), but added in a few important improvements for practice in adding better usability and security:

- To prevent the pesky browser warning about form resubmission when refreshing, I made use of the **POST-Redirect-GET (PRG) pattern**. This way, after submitting the form, the app redirects the user to a new page load, avoiding duplicate submissions.

- Wanted the QR code to persist across this redirect, used **Flask sessions** to temporarily store the generated QR code data between requests.

- To securely handle sessions, moved the secret key out of the code and into a `.env` file, loaded with `python-dotenv`. This keeps sensitive data out of version control and helps protect the app in real-world scenarios.

- Also added a `.gitignore` which excludes the virtual environment folder (`.venv`) and the `.env` file, preventing accidental commits of unnecessary or sensitive files.

- The app only shows the QR code after a successful form submission, keeping the UI clean and intuitive.
