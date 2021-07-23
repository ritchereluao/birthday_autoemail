import pandas
import datetime as dt
import random
import smtplib
from email.message import EmailMessage
from email.header import Header
from email.utils import formataddr

my_email = "email@gmail.com"
my_password = "emailemailpasswordpassword"

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

for each_person in data_dict:
    if each_person["month"] == today_month and each_person["day"] == today_day:
        birthday_month = each_person["month"]
        birthday_day = each_person["day"]
        birthday_name = each_person["name"]
        birthday_email = each_person["email"]

        random_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number}.txt") as letter_file:
            letter_contents = letter_file.readlines()
            birthday_letter = "".join(letter_contents).replace("[NAME]", birthday_name)

            msg = EmailMessage()
            msg["Subject"] = "Happy Birthday!"
            msg["From"] = formataddr((str(Header("FirstName LastName", "utf-8")), my_email))
            msg["To"] = birthday_email
            msg.set_content(f"{birthday_letter}")

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.send_message(msg)
