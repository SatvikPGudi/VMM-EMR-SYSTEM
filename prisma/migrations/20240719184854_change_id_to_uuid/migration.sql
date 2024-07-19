/*
  Warnings:

  - The primary key for the `Doctor` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - The primary key for the `Patient` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - The primary key for the `Soap_Note` table will be changed. If it partially fails, the table could be left without primary key constraint.

*/
-- DropForeignKey
ALTER TABLE "Soap_Note" DROP CONSTRAINT "Soap_Note_doctor_id_fkey";

-- DropForeignKey
ALTER TABLE "Soap_Note" DROP CONSTRAINT "Soap_Note_patient_id_fkey";

-- AlterTable
ALTER TABLE "Doctor" DROP CONSTRAINT "Doctor_pkey",
ALTER COLUMN "doctor_id" DROP DEFAULT,
ALTER COLUMN "doctor_id" SET DATA TYPE TEXT,
ADD CONSTRAINT "Doctor_pkey" PRIMARY KEY ("doctor_id");
DROP SEQUENCE "Doctor_doctor_id_seq";

-- AlterTable
ALTER TABLE "Patient" DROP CONSTRAINT "Patient_pkey",
ALTER COLUMN "patient_id" DROP DEFAULT,
ALTER COLUMN "patient_id" SET DATA TYPE TEXT,
ADD CONSTRAINT "Patient_pkey" PRIMARY KEY ("patient_id");
DROP SEQUENCE "Patient_patient_id_seq";

-- AlterTable
ALTER TABLE "Soap_Note" DROP CONSTRAINT "Soap_Note_pkey",
ALTER COLUMN "assignment_id" DROP DEFAULT,
ALTER COLUMN "assignment_id" SET DATA TYPE TEXT,
ALTER COLUMN "doctor_id" SET DATA TYPE TEXT,
ALTER COLUMN "patient_id" SET DATA TYPE TEXT,
ADD CONSTRAINT "Soap_Note_pkey" PRIMARY KEY ("assignment_id");
DROP SEQUENCE "Soap_Note_assignment_id_seq";

-- AddForeignKey
ALTER TABLE "Soap_Note" ADD CONSTRAINT "Soap_Note_doctor_id_fkey" FOREIGN KEY ("doctor_id") REFERENCES "Doctor"("doctor_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Soap_Note" ADD CONSTRAINT "Soap_Note_patient_id_fkey" FOREIGN KEY ("patient_id") REFERENCES "Patient"("patient_id") ON DELETE RESTRICT ON UPDATE CASCADE;
