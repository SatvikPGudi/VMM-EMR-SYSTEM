import asyncio
from typing import Any
from prisma import Prisma
from prisma.models import Doctor, Patient, SoapNote


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

    async def search_name(self, model: str, name: str) -> list[Any] | None:
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
    await client.remove_all("doctor")
    await client.remove_all("patient")

    # All new records
    await client.add_doctor("John Doe")
    await client.add_doctor("Peter Parker")
    await client.add_doctor("Frank John")

    # List all doctor
    all_doctors: list[Doctor] = await client.list_all("doctor")
    
    print("All Doctors:")
    print(*all_doctors, sep="\n")


    print()

    # Search records
    table_name = "doctor"
    query_name = "john"

    found_doctor: list[Doctor] = await client.search_name(table_name, query_name)

    print(f"Searching `{query_name}` in `{table_name}`:")
    print(found_doctor)
    

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
