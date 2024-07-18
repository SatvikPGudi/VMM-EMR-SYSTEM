import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
    const allDoctors = await prisma.doctor.findMany();
    console.log('All doctors:', allDoctors);
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
