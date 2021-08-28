import random
from utils import OSManager
from bs4 import *
import requests
import time
    

class Profile:
    def __init__(self, name = "", lastName = "", age = "", gender = ""):
        self.id = ""
        self.name = name
        self.lastName = lastName
        self.age = age
        self.birthDate = {
                        "Day": "0",
                        "Month": "0",
                        "Year": "0000"
                        }
        self.gender = gender
        self.password = ""
        self.path = ""

        self.generate_profile()

        
    def generate_profile(self):
        self.generate_id()
        self.generate_birthday()
        self.generate_password()
        self.generate_dir_path()
        self.generate_profile_pictures()
        self.generate_profile_txt()

    def generate_id(self):
        firstElement = self.gender
        secondElement = self.name[0].upper()
        thirdElement = self.name[-1].upper()
        fourthElement = self.lastName[0].upper()
        fifthElement = self.age

        self.id = firstElement + secondElement + thirdElement + fourthElement + fifthElement
        pass

    def generate_birthday(self):
        currentYear = "2021"
        months = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
                }

        birthMonthInt = random.randint(1,12)
        birthMonth = months[birthMonthInt]
        
        if birthMonthInt != 2:
            birthDay = random.randint(1,30)
        else:
            birthDay = random.randint(1,28)
        birthYear = str( int(currentYear) - int(self.age))

        self.birthDate["Day"] = str(birthDay)
        self.birthDate["Month"] = str(birthMonth)
        self.birthDate["Year"] = str(birthYear)
    
    def generate_password(self):
        firstElement = self.name[0].upper()
        secondElement = self.lastName
        thirdElement = "."
        fourthElement = str(random.randint(0,9))
        fifthElement = str(random.randint(0,9))
        sixthElement = str(random.randint(0,9))
        password = firstElement + secondElement + thirdElement + fourthElement + fifthElement + sixthElement

        self.password = password
    
    def generate_dir_path(self):
        OSManager.create_directory(f"./Profiles/{self.id}/")
        self.path = f"./Profiles/{self.id}/"

    def generate_profile_pictures(self):
        for i in range(5):
            url = "https://thispersondoesnotexist.com/"

            r2 = requests.get("https://thispersondoesnotexist.com/image").content
            try:
                try:
                    # print("DOWNLOAD")
                    # possibility of decode
                    r2 = str(r2, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    with open(f"./Profiles/{self.id}/{i}.jpg", "wb+") as f:
                        f.write(r2)

                    # counting number of image downloaded
            except:
                pass
            time.sleep(0.2)
    
    def generate_profile_txt(self):
        filePath = self.path + self.id + ".txt"
        file = OSManager.create_file(filePath, output = True)

        # self.id = ""
        # self.name = name
        # self.lastName = lastName
        # self.age = age
        # self.birthDate = {
        #                 "Day": "0",
        #                 "Month": "0",
        #                 "Year": "0000"
        #                 }
        # self.gender = gender
        # self.password = ""
        # self.path = ""
        firstLine =  f"ID        : {self.id} \n"
        secondLine = f"Name      : {self.name} \n"
        thirdLine =  f"lastName  : {self.lastName} \n"
        fourthLine = f"Age       : {self.age} \n"
        fifthLine =  f"Gender    : {self.gender} \n"
        sixthLine =  f"BirthDay  : {self.birthDate['Day']} \n"
        seventhLine =f"BirthMonth: {self.birthDate['Month']} \n"
        eightLine =  f"BirthYear : {self.birthDate['Year']} \n"
        ninethLine = f"Password  : {self.password} \n"

        file.write(firstLine)
        file.write(secondLine)
        file.write(thirdLine)
        file.write(fourthLine)
        file.write(fifthLine)
        file.write(sixthLine)
        file.write(seventhLine)
        file.write(eightLine)
        file.write(ninethLine)
        file.close()



        
        


if __name__ == "__main__":
    P1 = Profile(name = "Albert", lastName = "Navarrete", age = "20", gender = "M")
        