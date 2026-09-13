import asyncio
import csv
from telethon import TelegramClient

async def main():
    print("=" * 40)
    print("   TELEGRAM MEMBER MANAGER")
    print("=" * 40)

    api_id = int(input("\nEnter your Telegram API ID: ").strip())
    api_hash = input("Enter your Telegram API Hash: ").strip()

    source = input("\nEnter the source group username/link: ").strip()

    client = TelegramClient("telegram_member_manager", api_id, api_hash)

    print("\nConnecting to Telegram...")
    await client.start()

    print("Connected successfully!")
    print("\nRetrieving accessible members...")

    try:
        members = await client.get_participants(source)

        print(f"\nMembers found: {len(members)}")

        with open("members.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "User ID",
                "Username",
                "First Name",
                "Last Name"
            ])

            for user in members:
                writer.writerow([
                    user.id,
                    user.username or "",
                    user.first_name or "",
                    user.last_name or ""
                ])

        print("\nDone!")
        print("Members saved to: members.csv")

    except Exception as error:
        print("\nCould not retrieve members.")
        print("Reason:", error)

    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
