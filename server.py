from quart import Quart, request, render_template
from markupsafe import Markup
import utils
from database import VMMService
from datetime import datetime
import json

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


@app.route("/soap-notes/<uuid:soapnote_id>", methods=["GET", "POST"])
async def soap_notes(soapnote_id):
    soapnote_helper = utils.SoapNoteTemplate(db, str(soapnote_id))

    if request.method == "POST":
        form_data = await request.form
        await soapnote_helper.update_soapnote_content(form_data)

        return "OK"
    
    else:
        form_html = await soapnote_helper.get_form("template.json")

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

    form = await request.form

    test = json.dumps(form)

    print(test)

    return ""


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
