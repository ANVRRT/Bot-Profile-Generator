from dataset import Dataset
from profile import Profile

class Generator:
    def __init__(self,dataset, datasetLastName, gender):
        self.datasetNamesObject = dataset
        self.datasetLastNamesObject = datasetLastName
        self.gender = gender
        self.datasetName = self.datasetNamesObject.get_dataset()
        self.datasetLastName = self.datasetLastNamesObject.get_dataset()
        

    def generate_profiles(self):
        nameReg = self.datasetName.sample()
        lastNameReg = self.datasetLastName.sample()

        # (self, name = "", lastName = "", age = "", gender = "")

        name = nameReg.iloc[0]["Name"]
        age = str(nameReg.iloc[0]["Age"])
        # print(name)
        lastName = lastNameReg.iloc[0]["lastName"]
        P = Profile( name = name, lastName = lastName, age = age, gender = self.gender)
        del(P)

def generator_of_profiles(M, F, A, numberOfProfiles):
    GM = Generator(M, A, "M")
    GF = Generator(F, A, "F")
    
    for i in range(numberOfProfiles):
        GM.generate_profiles()
        GF.generate_profiles()


if __name__ == "__main__":
    M = Dataset("hombres.csv")
    # M.cleanse_dataset_names()

    F = Dataset("mujeres.csv")
    # F.cleanse_dataset_names()

    A = Dataset("apellidos.csv")
    # A.cleanse_dataset_lastnames()

    generator_of_profiles(M, F, A, 5)





    