import pandas as pd
from PythonLibraries_ForBegginers.os_manager import OSManager


class Dataset:
    
    def __init__(self, fileName):
        self.pathRaw = f"./RawDatasets/{fileName}"
        self.path = f"./Datasets/{fileName}"
        self.cleanse_dataset(self.pathRaw)
        # self.rawPath = 
        pass
    
    def cleanse_dataset(self, filePath):
        rawDataset = OSManager.open_pandas_csv_file(filePath)
        dataset = pd.DataFrame({
                                "Name": [],
                                "Age": []
                                })

        for index, row in rawDataset.iterrows():
            if row["nombre"] != "" and row["edad_media"] != "":
                names = row["nombre"].lower().split()
                newName = []
                for name in names:
                    newName.append(name[0].upper()+name[1:])
                row["nombre"] = " ".join(newName)
                row = pd.DataFrame({
                                    "Name": [row["nombre"]],
                                    "Age": [str(int(row["edad_media"]))]
                                    })
                dataset = dataset.append(row)
        
        dataset.to_csv(self.path, index = False)
        # print(dataset)
    

class Profile:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.lastName = ""
        self.birthDay = {
                        "Day": "0",
                        "Month": "0",
                        "Year": "0000"
                        }
        self.password = ""

        pass

    pass

if __name__ == "__main__":
    Test = Dataset("hombres.csv")
    Test2 = Dataset("mujeres.csv")

    