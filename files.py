import os

schema_dir = "schema"
sample_data_dir = "sample_data"

def get_schema():
    return get_data(schema_dir, ".sql")

def get_sampel_data():
    return get_data(sample_data_dir, ".csv")

def get_data(dir, ext):
    data = ""

    for fname in os.listdir(dir):
        if fname.endswith(ext):
            with open(dir + "/" + fname, "r") as f:
                print("reading " + fname )
                data += "\n" + f.read()

    return data
