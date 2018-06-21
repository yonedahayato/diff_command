import pandas as pd

class Diff_Line:
    def __init__(self):
        self.file_name1 = "memo_after_S.csv"
        self.file_name2 = "memo_before_S.csv"

        self.ignore_col = [1]

    def read_csv(self):
        self.data_df1 = pd.read_csv(self.file_name1, header=None)
        self.data_df2 = pd.read_csv(self.file_name2, header=None)

        self.data_df1 = self.data_df1.fillna(0)
        self.data_df2 = self.data_df2.fillna(0)

        self.min_len = min(len(self.data_df1), len(self.data_df2))

    def diff(self):
        self.read_csv()
        diff_list = []

        col1 = list(self.data_df1.columns)
        col2 = list(self.data_df2.columns)

        col1.remove(self.ignore_col)
        col2.remove(self.ignore_col)

        for i in range(self.min_len):
            line1 = self.data_df1.iloc[i, col1]
            line2 = self.data_df2.iloc[i, col2]

            diff = line1 == line2
            diff_list.append(diff.all())
            if diff.all() == False:
                print(line1)
                print(line2)

        print(diff_list)
def main():
    dl = Diff_Line()
    dl.diff()

if __name__ == "__main__":
    main()
