CREATE DATABASE emr_system;

\c emr_system;

CREATE TABLE Doctors (
    doctor_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE
);


CREATE TABLE Soap_Notes (
    assignment_id SERIAL PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    date_of_visit DATE,
    chief_complaint TEXT,
    hpi TEXT,
    past_medical_history TEXT,
    surgical_history TEXT,
    family_history TEXT,
    social_history TEXT,
    allergies TEXT,
    medications TEXT,
    review_of_systems TEXT,
    height FLOAT,
    weight FLOAT,
    bmi FLOAT,
    blood_pressure VARCHAR(50),
    temperature FLOAT,
    pulse INT,
    o2_oximeter FLOAT,
    physical_exam TEXT,
    test_results TEXT,
    assessment TEXT,
    plan TEXT,
    follow_up TEXT,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
