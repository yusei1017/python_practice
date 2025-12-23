import pandas as pd

def load_scores(csv_path):
    df=pd.read_csv(csv_path)
    return df
def show_status(df):       #df a+b() retrun a+b
    subjects = ["math", "english", "japanese"]
    print("=== 平均 ===")
    print(df[subjects].mean())
    print("=== 最大 ===")
    print(df[subjects].max())
    print("=== 最小 ===")
    print(df[subjects].min())

def filter_math(df):
    return df[df["math"]>=80]