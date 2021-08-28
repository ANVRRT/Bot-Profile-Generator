import pandas as pd
from utils import OSManager

class Dataset:
    
    def __init__(self, fileName): # names = True
        self.pathRaw = f"./RawDatasets/{fileName}"
        self.path = f"./Datasets/{fileName}"  

    def get_numberOf_registries(self):
        return len(self.pandasDataset.index)

    def get_dataset(self):
        return OSManager.open_pandas_csv_file(self.path)


    def cleanse_dataset_names(self):
        rawDataset = OSManager.open_pandas_csv_file(self.pathRaw)
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
        self.pandasDataset = dataset

    def cleanse_dataset_lastnames(self):
        rawDataset = OSManager.open_pandas_csv_file(self.pathRaw)
        dataset = pd.DataFrame({
                                "lastName": []
                                })

        for index, row in rawDataset.iterrows():
            if row["apellido"] != "":
                # print(f"Apellido: {row['apellido']}")
                lastName = row["apellido"].lower()
                row["apellido"] = lastName[0].upper()+lastName[1:]

                row = pd.DataFrame({
                                    "lastName": [row["apellido"]]
                                    })
                dataset = dataset.append(row)
        
        dataset.to_csv(self.path, index = False)
        self.pandasDataset = dataset