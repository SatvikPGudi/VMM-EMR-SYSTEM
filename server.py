from flask import Flask, request, render_template, jsonify, redirect, url_for
from markupsafe import Markup
import parse_template

import json

app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates",
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soap-notes")
def soap_notes():
    template = parse_template.ParseTemplate("template.json")
    form_html = template.get_form()

    form_content = Markup(form_html)
    return render_template("soap-notes.html", form_content=Markup(form_content))


@app.route("/patient-portal", methods=["GET", "POST"])
def patient_portal():
    # I am sorry for this horrible test code
    sample_data = """
    [
        {
            "PatientID": "1",
            "LastName": "Smith",
            "FirstName": "John",
            "DateOfBirth": "1980-05-15",
            "Sex": "Male"
        },
        {
            "PatientID": "2",
            "LastName": "Doe",
            "FirstName": "Jane",
            "DateOfBirth": "1992-08-22",
            "Sex": "Female"
        },
        {
            "PatientID": "3",
            "LastName": "Johnson",
            "FirstName": "Emily",
            "DateOfBirth": "1975-12-30",
            "Sex": "Female"
        }
    ]
    """

    json_data = json.loads(sample_data)

    table_head = []
    table_body = []

    for item in json_data[0].keys():
        table_head.append(f"<th>{item}</th>")

    for patient in json_data:
        patient_data = []
        for data in patient.values():
            patient_data.append(f"<td>{data}</td>")

        patient_html = "\n".join(patient_data)

        table_body.append(f"<tr>{patient_html}</tr>")

    table_head_html = "<tr>" + "\n".join(table_head) + "</tr>"
    table_body_html = "\n".join(table_body)

    print(table_head_html)
    print(table_body_html)

    if request.method == "POST":
        return render_template(
            "patient-portal.html",
            table_head=Markup(table_head_html),
            table_body=Markup(table_body_html),
        )
    return render_template("patient-portal.html")


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
