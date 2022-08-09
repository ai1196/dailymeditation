import argparse
import datetime
import yagmail
import dailymeditation

parser = argparse.ArgumentParser(description="CLI for the Meditation application.")
parser.add_argument("--username", type=str, help="nyustern.python.summer2022@gmail.com", required=True)
parser.add_argument("--app_password", type=str, help="kxrcubvacrxpaofr", required=True)
parser.add_argument("--recipients", type=str, help="nyustern.python.summer2022@gmail.com", required=True)

CURRENT_MEDITATION = dailymeditation.MEDITATION

if __name__ == "__main__":
    # Parse the command line arguments
    args = parser.parse_args()

    # Get today as a weekday integer
    today = datetime.datetime.today().weekday()

    # See if today is a meditation day
    if today in CURRENT_MEDITATION.keys():
        meditation = CURRENT_MEDITATION.get(today)
        subject = f"MEDITATION: {meditation.name}"

        contents = [meditation.as_html().replace("\n","")]

        with yagmail.SMTP(user=args.username, password=args.app_password) as yag:
            for recipient in args.recipients.split(","):
                yag.send(to=recipient, subject=subject, contents=contents)