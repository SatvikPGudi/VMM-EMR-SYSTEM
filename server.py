from quart import Quart, request, render_template, jsonify, redirect, url_for
from markupsafe import Markup
import utils
from database import VMMService
from datetime import datetime

app = Quart(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates",
)

db = VMMService()

@app.template_global("get_year")
def get_year():
    return datetime.today().year


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
    template = utils.SoapNoteTemplate("template.json")
    form_html = template.get_form()

    form_content = Markup(form_html)
    return await render_template("soap-notes.html", form_content=Markup(form_content))


@app.route("/patient-portal", methods=["GET", "POST"])
async def patient_portal():
    if request.method == "POST":
        patient_name = (await request.form).get("name-query", "")

        portal_helper = utils.PatientPortal(db)
        table_body_html = await portal_helper.get_patient_table(patient_name)

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
