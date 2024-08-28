from flask import Flask, request, render_template, jsonify
from markupsafe import Markup
import parse_template


app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates",
)


@app.route("/")
def index():
    template = parse_template.ParseTemplate("template.json")
    form_html = template.get_form()
    form_content = Markup(form_html)
    return render_template("dynamic-index.html", form_content=Markup(form_content))


# Endpoint to submits patient data
@app.post("/api/submit")
def submit():
    # TODO: implement data push function

    for key, value in request.form.items():
        print(f"{key}: {value}")

    return jsonify(request.form)


@app.post("/api/retrieve")
def retrieve():
    # TODO: implement retrieve function
    pass


if __name__ == "__main__":
    app.run(debug=True)
