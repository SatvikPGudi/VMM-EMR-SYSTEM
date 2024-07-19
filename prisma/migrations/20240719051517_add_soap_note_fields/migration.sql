-- CreateTable
CREATE TABLE "Doctor" (
    "doctor_id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,

    CONSTRAINT "Doctor_pkey" PRIMARY KEY ("doctor_id")
);

-- CreateTable
CREATE TABLE "Patient" (
    "patient_id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "dob" TIMESTAMP(3),

    CONSTRAINT "Patient_pkey" PRIMARY KEY ("patient_id")
);

-- CreateTable
CREATE TABLE "Soap_Note" (
    "assignment_id" SERIAL NOT NULL,
    "doctor_id" INTEGER NOT NULL,
    "patient_id" INTEGER NOT NULL,
    "date_of_visit" TIMESTAMP(3) NOT NULL,
    "chief_complaint" TEXT,
    "hpi" TEXT,
    "past_medical_history" TEXT,
    "surgical_history" TEXT,
    "family_history" TEXT,
    "social_history" TEXT,
    "allergies" TEXT,
    "medications" TEXT,
    "review_of_systems" TEXT,
    "height" DOUBLE PRECISION,
    "weight" DOUBLE PRECISION,
    "bmi" DOUBLE PRECISION,
    "blood_pressure" TEXT,
    "temperature" DOUBLE PRECISION,
    "pulse" INTEGER,
    "o2_oximeter" DOUBLE PRECISION,
    "physical_exam" TEXT,
    "test_results" TEXT,
    "assessment" TEXT,
    "plan" TEXT,
    "follow_up" TEXT,

    CONSTRAINT "Soap_Note_pkey" PRIMARY KEY ("assignment_id")
);

-- AddForeignKey
ALTER TABLE "Soap_Note" ADD CONSTRAINT "Soap_Note_doctor_id_fkey" FOREIGN KEY ("doctor_id") REFERENCES "Doctor"("doctor_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Soap_Note" ADD CONSTRAINT "Soap_Note_patient_id_fkey" FOREIGN KEY ("patient_id") REFERENCES "Patient"("patient_id") ON DELETE RESTRICT ON UPDATE CASCADE;
