import Image from "next/image";

export default function Home() {
  return (
    <div>
      <h3>
        Date of clinic visit:
        <br />
        <br />
        Patient name:
        <br />
        <br />
        Date of birth:
      </h3>

      <form className="alignment" action="/submit" method="POST">
        <hr />

        <div>
          <h1 className="title">Subjective</h1>

          <h2 className="pt-4">
            <label htmlFor="chief-complaint">Chief Complaint</label>
          </h2>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="chief-complaint"
            name="chief-complaint"
          ></textarea>

          <h2 className="pt-4">
            <label htmlFor="hpi">HPI</label>
          </h2>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="hpi"
            name="hpi"
          ></textarea>

          <h2 className="pt-8">History:</h2>

          <h4 className="pt-2">
            <label htmlFor="medical-history">Past Medical History</label>
          </h4>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="medical-history"
            name="medical-history"
          ></textarea>

          <h4 className="pt-2">
            <label htmlFor="surgical-history">Surgical History</label>
          </h4>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="surgical-history"
            name="surgical-history"
          ></textarea>

          <h4 className="pt-2">
            <label htmlFor="family-history">Family History</label>
          </h4>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="family-history"
            name="family-history"
          ></textarea>

          <h4 className="pt-2">
            <label htmlFor="social-history">Social History</label>
          </h4>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="social-history"
            name="social-history"
          ></textarea>

          <h2 className="pt-8">
            <label htmlFor="allergies">Allergies</label>
          </h2>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="allergies"
            name="allergies"
          ></textarea>

          <h2 className="pt-4">
            <label htmlFor="medications">Medications</label>
          </h2>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="medications"
            name="medications"
          ></textarea>

          <h2 className="pt-4" id="ROS">
            <label htmlFor="symptom-review">Review of Systems</label>
          </h2>
          <textarea
            className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
            rows={3}
              cols={60}
            id="symptom-review"
            name="symptom-review"
          ></textarea>
        </div>

        <hr />

        <div>
          <h1 className="title pt-12">Objective</h1>

          <h2 className="pt-4">Vital Signs:</h2>
          <div>
            <div className="pt-2">
              <label htmlFor="height" className="label">Height:</label>
              <input
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                type="text"
                id="height"
                name="height"
              />
            </div>
            <br />
            <div>
              <label htmlFor="weight" className="label">Weight:</label>
              <input
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                type="text"
                id="weight"
                name="weight"
              />
            </div>
            <br />
            <div>
              <label htmlFor="bmi" className="label">BMI:</label>
              <input
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                type="text"
                id="bmi"
                name="bmi"
              />
            </div>
            <br />
            <div>
              <label htmlFor="blood-pressure" className="label">Blood Pressure:</label>
              <input
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                type="text"
                id="blood-pressure"
                name="blood-pressure"
              />
            </div>
            <br />
            <div>
              <label htmlFor="temp" className="label">Temperature:</label>
              <input
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                type="text"
                id="temp"
                name="temp"
              />
            </div>
            <br />
            <div>
              <label htmlFor="pulse" className="label">Pulse:</label>
              <input
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                type="text"
                id="pulse"
                name="pulse"
              />
            </div>
            <br />
            <div>
              <label htmlFor="oxygen" className="label">O2 Oximeter:</label>
              <input
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                type="text"
                id="oxygen"
                name="oxygen"
              />
            </div>
          </div>

          <br />

          <div>
            <h2 className="pt-4">Physical Exam:</h2>
            <div className="pt-2">
              <h4><label>Constitutional</label></h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
               cols={60}
                id="constitutional"
              ></textarea>
            </div>
            <div className="pt-2">
              <h4>
                <label htmlFor="ent">ENT</label>
              </h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
               cols={60}
                id="ent"
                name="ent"
              ></textarea>
            </div>
            <div className="pt-2">
              <h4>
                <label htmlFor="respiratory">Respiratory</label>
              </h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
               cols={60}
                id="respiratory"
                name="respiratory"
              ></textarea>
            </div>
            <div className="pt-2">
              <h4>
                <label htmlFor="cardio">Cardio</label>
              </h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
                cols={60}
                id="cardio"
                name="cardio"
              ></textarea>
            </div>
            <div className="pt-2">
              <h4>
                <label htmlFor="cal">Cal</label>
              </h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
                cols={60}
                id="cal"
                name="cal"
              ></textarea>
            </div>
            <div className="pt-2">
              <h4>
                <label htmlFor="skin">Skin</label>
              </h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
                cols={60}
                id="skin"
                name="skin"
              ></textarea>
            </div>
            <div className="pt-2">
              <h4>
                <label htmlFor="extremities">Extremities</label>
              </h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
                cols={60}
                id="extremities"
                name="extremities"
              ></textarea>
            </div>
            <div className="pt-2">
              <h4>
                <label htmlFor="neuro">Neuro</label>
              </h4>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={3}
                cols={60}
                id="neuro"
                name="neuro"
              ></textarea>
            </div>
            <div className="pt-4">
              <h2>
                <label htmlFor="test-results">Test Results</label>
              </h2>
              <input className="pl-20" type="file" id="test-results" name="test-results" />
            </div>
          </div>
          <br />

          <div className="pt-4">
            <div>
              <h1 className="title">
                <label htmlFor="assessment">Assessment</label>
              </h1>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={20}
                cols={110}
                id="assessment"
                name="assessment"
              ></textarea>
            </div>
            <br />
            <div>
              <h1 className="title">
                <label htmlFor="plan">Plan</label>
              </h1>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={20}
                cols={110}
                id="plan"
                name="plan"
              ></textarea>
            </div>
            <br />
            <div>
              <h1 className="title">
                <label htmlFor="follow-up">Follow Up</label>
              </h1>
              <textarea
                className="transition-all duration-500 rounded-md border-2 border-gray-300 hover:border-black"
                rows={20}
                cols={110}
                id="follow-up"
                name="follow-up"
              ></textarea>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
}
