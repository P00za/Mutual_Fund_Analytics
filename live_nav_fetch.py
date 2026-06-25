import requests
import pandas as pd
from pathlib import Path

# Create raw data folder
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Scheme codes
schemes = {
    "hdfc_top_100_direct": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

fund_master_records = []
all_nav_data = []

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching data for: {scheme_name}")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meta = data.get('meta',{})
        nav_data = data.get("data", [])

        # Convert NAV history to DataFrame
        
        df = pd.DataFrame(nav_data)

        # Add scheme details
        df["scheme_code"] = scheme_code
        df["scheme_name"] = data.get("meta", {}).get("scheme_name", scheme_name)
        df["fund_house"] = data.get("meta", {}).get("fund_house", "Unknown")
        df["scheme_category"] = data.get("meta", {}).get("scheme_category", "Unknown")
        df["scheme_type"] = data.get("meta", {}).get("scheme_type", "Unknown")

        # Save  Individual NAV CSV file
        file_path = RAW_DIR / f"{scheme_name}_nav.csv"
        df.to_csv(file_path, index=False)

        # Store for combined nav_history
        all_nav_data.append(df)

        # Store fund master metadata

        fund_master_records.append({
            "scheme_code" : scheme_code,
            "scheme_name" : data.get("meta", {}).get("scheme_name", scheme_name),
            "fund_house":data.get("meta", {}).get("fund_house", "Unknown"),
            "scheme_category" :data.get("meta", {}).get("scheme_category", "Unknown"),
            "scheme_type": data.get("meta", {}).get("scheme_type", "Unknown"),

                
        })

        print(f"Saved: {file_path}")
        print("Shape:", df.shape)
        print("Head:")
        print(df.head())

    else:
        print(f"Failed to fetch {scheme_name}. Status code: {response.status_code}")


# Create combined nav_history.csv
if all_nav_data:
    nav_history = pd.concat(all_nav_data, ignore_index=True)
    nav_history.to_csv(RAW_DIR / "nav_history.csv", index=False)
    print("\nSaved: nav_history.csv")
    print("nav_history shape:", nav_history.shape)

# Create fund_master.csv
fund_master = pd.DataFrame(fund_master_records)
fund_master.to_csv(RAW_DIR / "fund_master.csv", index=False)
print("\nSaved: fund_master.csv")
print(fund_master)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["scheme_category"].unique())

print("\nScheme Types:")
print(fund_master["scheme_type"].unique())


print("\nAll NAV files fetched and saved successfully.")