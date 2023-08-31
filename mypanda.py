import pandas
import os


def main():
    df = pandas.read_csv(os.path.join(os.path.dirname(__file__), "data.csv"))
    df.to_csv(os.path.join(os.path.dirname(__file__), "data_out.csv"))


main()
