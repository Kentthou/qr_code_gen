from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os, io, qrcode, base64

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        if not link:
            return redirect(url_for("index"))
        
        # Generate QR
        img = qrcode.make(link)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        img_data = f"data:image/png;base64,{img_base64}"

        # Store result in session
        session["qr_data"] = img_data
        return redirect(url_for("index"))

    qr_data = session.pop("qr_data", None)
    return render_template("index.html", data=qr_data)

if __name__ == "__main__":
    app.run(debug=True)
