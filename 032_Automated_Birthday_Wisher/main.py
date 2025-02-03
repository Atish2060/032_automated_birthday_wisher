import pandas
import _datetime as dt
from random import  choice
import smtplib
PLACEHOLDER = "[NAME]"
AGE = "[AGE]"
email = "atishtest2060@gmail.com"
password = "pzch mfxp mvwn fiwu"


#choosing the letters form the list of letters
list_of_letters = ["./letter_templates/letter_1.txt","./letter_templates/letter_2.txt","./letter_templates/letter_3.txt"]
chose_letter = choice(list_of_letters)
# print(chose_letter)

#choosing the today's month and day
today = dt.datetime.now()
year = today.year
month = today.month
day = today.day

#reading the birthdays.csv file
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv and sending the mail
for n in range(0,len(data_dict)):
    if month == data_dict[n]["month"] and day == data_dict[n]["day"]:
        age = str(year - data_dict[n]["year"])
        with open(chose_letter, mode ="r") as file:
            content = file.read()
            name = data_dict[n]["name"].strip()
            new_letter = content.replace(PLACEHOLDER, name)
            new_letter1 = new_letter.replace(AGE, age)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user= email, password= password)
            connection.sendmail(from_addr=email,
                                to_addrs=data_dict[n]["email"],
                                msg=f"Subject:Happy Birthday !!\n\n{new_letter1}")
        print(f'Letter sent to {data_dict[n]["name"]}')
