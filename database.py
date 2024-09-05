import asyncio
from typing import Any
from prisma import Prisma
from prisma.models import Doctor, Patient, SoapNote
from datetime import datetime


class VMMService:
    def __init__(self) -> None:
        self.prisma = Prisma()

    async def connect(self) -> None:
        await self.prisma.connect()

    async def disconnect(self) -> None:
        await self.prisma.disconnect()

    def get_model(self, model: str) -> type[Any] | None:
        try:
            target_attribute = getattr(self.prisma, model.lower())
            return target_attribute
        except AttributeError as e:
            print(f"Model '{model}' not found on 'self.prisma'.")
            return None

    async def add_doctor(self, name: str) -> Doctor:
        new_doctor: Doctor = await self.prisma.doctor.create(
            data={
                "name": name,
            }
        )

        return new_doctor

    async def add_patient(
        self,
        doctor: Doctor,
        name: str,
        sex: str,
        dob: datetime | None = None,
    ) -> Patient:
        new_patient = await self.prisma.patient.create(
            data={
                "name": name,
                "dob": dob.astimezone().isoformat() if dob else None,
                "sex": sex,
                "doctor": {
                    "connect": {"id": doctor.id},
                },
            },
        )

        return new_patient

    async def list_doctor_patients(self, doctor: Doctor) -> list[Patient]:
        query_result: list[Patient] = await self.prisma.patient.find_many(
            where={
                "doctorId": doctor.id,
            }
        )

        return query_result

    async def search_unique(self, model: str, **kwargs: dict[str, Any]) -> Any | None:
        query_result: Any = await self.get_model(model).find_unique(
            where=kwargs,
        )

        return query_result

    async def search_many(self, model: str, **kwargs: dict[str, Any]) -> list[Any] | None:
        query_result: list[Any] = await self.get_model(model).find_many(
            where=kwargs,
        )

        return query_result

    async def search_name(self, model: str, name: str) -> Any | None:
        query_result: list[Any] = await self.get_model(model).find_many(
            where={
                "name": {
                    "contains": name,
                    "mode": "insensitive",
                },
            }
        )

        return query_result

    async def list_all(self, model: str) -> list[Any] | None:
        query_result: list[Any] = await self.get_model(model).find_many()
        return query_result

    async def remove_all(self, model: str) -> None:
        await self.get_model(model).delete_many()


async def main() -> None:
    client = VMMService()

    await client.connect()

    # Remove all records
    # await client.remove_all("doctor")
    # await client.remove_all("patient")

    # All new records
    new_doc = await client.add_doctor("John Doe")

    new_patient_a = await client.add_patient(
        new_doc, "Meow", "Male", datetime(2001, 5, 24)
    )

    new_patient_b = await client.add_patient(
        new_doc, "Wolf", "Female", datetime(2008, 9, 12)
    )

    print(new_doc)
    print()
    print(new_patient_a)
    print(new_patient_b)
    print()

    # List all patients assigned to new_doc

    searched = await client.list_patient(new_doc)

    for i in searched:
        print(i.model_dump_json())

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
