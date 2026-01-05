import pandas as pd


def kpis_by_borough(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute core operational KPIs by borough.
    """
    out = (
        df.groupby("borough", as_index=False)
        .agg(
            incidents=("incident_id", "count"),
            median_response_time_s=("response_time_s", "median"),
            p90_response_time_s=("response_time_s", lambda x: x.quantile(0.90)),
        )
    )

    # Add minutes for readability in Power BI
    out["median_response_time_min"] = out["median_response_time_s"] / 60
    out["p90_response_time_min"] = out["p90_response_time_s"] / 60

    # Sort by worst median response time (descending)
    out = out.sort_values("median_response_time_s", ascending=False)

    return out


if __name__ == "__main__":
    df = pd.read_csv("data/processed/lfb_incidents_clean.csv")

    kpi_table = kpis_by_borough(df)
    kpi_table.to_csv("data/processed/kpis_by_borough.csv", index=False)

    print("Saved: data/processed/kpis_by_borough.csv")
    print(kpi_table.head(10))
