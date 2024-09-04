from quart import Quart, request, render_template, jsonify, redirect, url_for
from markupsafe import Markup
import parse_template
from database import VMMService

app = Quart(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates",
)

db = VMMService()


@app.before_serving
async def startup():
    await db.connect()


@app.after_serving
async def shutdown():
    await db.disconnect()


@app.route("/")
async def index():
    return await render_template("index.html")


@app.route("/soap-notes")
async def soap_notes():
    template = parse_template.ParseTemplate("template.json")
    form_html = template.get_form()

    form_content = Markup(form_html)
    return await render_template("soap-notes.html", form_content=Markup(form_content))


@app.route("/patient-portal", methods=["GET", "POST"])
async def patient_portal():
    if request.method == "POST":
        name_query = (await request.form).get("name-query", "")
        query_result = await db.search_name("patient", name_query)

        table_body = []

        for patient in query_result:
            patient_id = patient.id[:5] + " ..."
            name = patient.name
            date_of_birth = patient.dob.date()
            sex = patient.sex

            assigned_doctor = await db.search_unique("doctor", id=patient.doctorId)
            doctor_name = assigned_doctor.name

            patient_data = [patient_id, name, name, date_of_birth, sex, doctor_name]

            patient_data = [f"<td>{data}</td>" for data in patient_data]

            patient_html = "\n".join(patient_data)

            table_body.append(f"<tr>{patient_html}</tr>")

        table_body_html = "\n".join(table_body)

        return await render_template(
            "patient-portal.html",
            table_body=Markup(table_body_html),
        )

    return await render_template("patient-portal.html")


# Endpoint to submits patient data
@app.post("/api/submit")
async def submit():
    # TODO: implement data push function

    for key, value in await request.form.items():
        print(f"{key}: {value}")

    return jsonify(await request.form)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
