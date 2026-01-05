import pandas as pd


def load_lfb_data(path: str) -> pd.DataFrame:
    """
    Load raw London Fire Brigade data and perform basic checks.
    """
    df = pd.read_csv(path)

    # Basic data quality check
    if df.empty:
        raise ValueError("The dataset is empty")

    return df


if __name__ == "__main__":
    df = load_lfb_data("data/raw/lfb_incidents.csv")
    print(df.head())
