import pandas as pd


REQUIRED_COLUMNS = [
    "incident_id",
    "borough",
    "call_datetime",
    "turnout_datetime",
    "arrival_datetime",
]


def parse_datetimes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse key datetime columns safely.
    """
    df = df.copy()
    for col in ["call_datetime", "turnout_datetime", "arrival_datetime"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def compute_response_time_seconds(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute response time in seconds: arrival - call.
    """
    df = df.copy()
    df["response_time_s"] = (df["arrival_datetime"] - df["call_datetime"]).dt.total_seconds()
    return df


def clean_lfb_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning + data quality rules for LFB operational analysis.
    """
    # Keep only required columns if present
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df[REQUIRED_COLUMNS].copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Parse datetimes
    df = parse_datetimes(df)

    # Drop rows with invalid datetimes
    df = df.dropna(subset=["call_datetime", "arrival_datetime", "borough", "incident_id"])

    # Compute response time
    df = compute_response_time_seconds(df)

    # Remove impossible / extreme values (basic rule-of-thumb)
    df = df[(df["response_time_s"] > 0) & (df["response_time_s"] < 4 * 60 * 60)]

    # Normalize borough casing
    df["borough"] = df["borough"].astype(str).str.strip().str.title()

    return df


if __name__ == "__main__":
    df_raw = pd.read_csv("data/raw/lfb_incidents.csv")
    df_clean = clean_lfb_data(df_raw)

    df_clean.to_csv("data/processed/lfb_incidents_clean.csv", index=False)
    print("Saved: data/processed/lfb_incidents_clean.csv")
