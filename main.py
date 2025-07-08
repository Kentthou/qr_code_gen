from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        if not link:
            return render_template("index.html", data=None)

        # Generate QR code
        img = qrcode.make(link)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        img_data = f"data:image/png;base64,{img_base64}"

        return render_template("index.html", data=img_data)

    return render_template("index.html", data=None)

if __name__ == "__main__":
    app.run(debug=True)
