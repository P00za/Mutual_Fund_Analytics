
import pandas as pd

print("*******Data Ingestion Started*******")

print("="*50)
print("\n ***** 01_fund_master.csv *****\n")
print("="*50)

fund_master = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\01_fund_master.csv")
print("Top 5 rows and columns of the dataset : \n",fund_master.head())
print("Shape of the dataset : \n",fund_master.shape)
print("Data types of the dataset : \n",fund_master.dtypes)
print("Columns of the dataset : \n",fund_master.columns.to_list())

# Clean column names for easier use
fund_master.columns = (
    fund_master.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Column Names:")
print(fund_master.columns.tolist())

# Unique values exploration
print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nTotal Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Category:")
print(fund_master["risk_category"].unique())

# AMFI scheme code understanding
print("\nAMFI Scheme Name Sample:")
print(fund_master["scheme_name"].head(10))

print("\nScheme Name Data Type:")
print(fund_master["scheme_name"].dtype)

print("\nMissing Values in Fund Master:")
print(fund_master.isnull().sum())

print("="+"="*50)
print("\n ***** 02_nav_history.csv *****\n")
print("="+"="*50)

nav_history = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\02_nav_history.csv")
print("Top 5 rows and columns of the dataset : \n",nav_history.head())
print("Shape of the dataset : \n",nav_history.shape)
print("Data types of the dataset : \n",nav_history.dtypes)
print("Columns of the dataset : \n",nav_history.columns)

print("\n" + "="*60)
print("STEP 7: AMFI CODE VALIDATION")
print("="*60)

# Clean column names for nav_history also
nav_history.columns = (
    nav_history.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nFund Master Columns:")
print(fund_master.columns.tolist())

print("\nNAV History Columns:")
print(nav_history.columns.tolist())


# Convert scheme codes to string for safe comparison
fund_master["amfi_code"] = fund_master["amfi_code"].astype(str).str.strip()
nav_history["amfi_code"] = nav_history["amfi_code"].astype(str).str.strip()

# Unique scheme codes
fund_master_codes = set(fund_master["amfi_code"].unique())
nav_history_codes = set(nav_history["amfi_code"].unique())

# Validation
matched_codes = fund_master_codes.intersection(nav_history_codes)
missing_codes = fund_master_codes - nav_history_codes

print("\nTotal unique scheme codes in fund_master:")
print(len(fund_master_codes))

print("\nTotal unique scheme codes in nav_history:")
print(len(nav_history_codes))


print("\nMatched scheme codes:")
print(len(matched_codes))

print("\nMissing scheme codes from nav_history:")
print(len(missing_codes))

if len(missing_codes) > 0:
    print("\nSample missing amfi codes:")
    print(list(missing_codes)[:20])
else:
    print("\nAll fund_master amfi codes exist in nav_history.")

# Data quality summary
print("\n" + "="*60)
print("DATA QUALITY SUMMARY")
print("="*60)

print(f"Total schemes in fund_master: {len(fund_master_codes)}")
print(f"Total schemes in nav_history: {len(nav_history_codes)}")
print(f"Matched schemes: {len(matched_codes)}")
print(f"Missing schemes in nav_history: {len(missing_codes)}") 

if len(missing_codes) == 0:
    print("Result: Data quality is good. Every fund_master amfi code exists in nav_history.")
else:
    print("Result: Some scheme codes from fund_master are missing in nav_history. These should be reviewed.")


print("="+"="*50)
print("\n ***** 03_aum_by_fund_house.csv *****\n")
print("="+"="*50)

aum_by_fund_house = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\03_aum_by_fund_house.csv")
print("Top 5 rows and columns of the dataset : \n",aum_by_fund_house.head())
print("Shape of the dataset : \n",aum_by_fund_house.shape)
print("Data types of the dataset : \n",aum_by_fund_house.dtypes)
print("Columns of the dataset : \n",aum_by_fund_house.columns)

print("="+"="*50)
print("\n ***** 04_monthly_sip_inflows.csv *****\n")
print("="+"="*50)

monthly_sip_inflows = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\04_monthly_sip_inflows.csv")
print("Top 5 rows and columns of the dataset : \n",monthly_sip_inflows.head())
print("Shape of the dataset : \n",monthly_sip_inflows.shape)
print("Data types of the dataset : \n",monthly_sip_inflows.dtypes)
print("Columns of the dataset : \n",monthly_sip_inflows.columns)

print("="+"="*50)
print("\n ***** 05_category_inflows.csv *****\n")
print("="+"="*50)

category_inflows = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\05_category_inflows.csv")
print("Top 5 rows and columns of the dataset : \n",category_inflows.head())
print("Shape of the dataset : \n",category_inflows.shape)
print("Data types of the dataset : \n",category_inflows.dtypes)
print("Columns of the dataset : \n",category_inflows.columns)

print("="+"="*50)
print("\n ***** 06_industry_folio_count.csv *****\n")
print("="+"="*50)

industry_folio_count = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\06_industry_folio_count.csv")
print("Top 5 rows and columns of the dataset : \n",industry_folio_count.head())
print("Shape of the dataset : \n",industry_folio_count.shape)
print("Data types of the dataset : \n",industry_folio_count.dtypes)
print("Columns of the dataset : \n",industry_folio_count.columns)

print("="+"="*50)
print("\n ***** 07_scheme_performance.csv *****\n")
print("="+"="*50)

scheme_performance = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\07_scheme_performance.csv")
print("Top 5 rows and columns of the dataset : \n",scheme_performance.head())
print("Shape of the dataset : \n",scheme_performance.shape)
print("Data types of the dataset : \n",scheme_performance.dtypes)
print("Columns of the dataset : \n",scheme_performance.columns)

print("="+"="*50)
print("\n ***** 08_investor_transactions.csv *****\n")
print("="+"="*50)

investor_transactions = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\08_investor_transactions.csv")
print("Top 5 rows and columns of the dataset : \n",investor_transactions.head())
print("Shape of the dataset : \n",investor_transactions.shape)
print("Data types of the dataset : \n",investor_transactions.dtypes)
print("Columns of the dataset : \n",investor_transactions.columns)

print("="+"="*50)
print("\n ***** 09_portfolio_holdings.csv *****\n")
print("="+"="*50)

portfolio_holdings = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\09_portfolio_holdings.csv")
print("Top 5 rows and columns of the dataset : \n",portfolio_holdings.head())
print("Shape of the dataset : \n",portfolio_holdings.shape)
print("Data types of the dataset : \n",portfolio_holdings.dtypes)
print("Columns of the dataset : \n",portfolio_holdings.columns)

print("="+"="*50)
print("\n ***** 10_benchmark_indices.csv *****\n")
print("="+"="*50)

benchmark_indices = pd.read_csv("C:\\Users\\p00za\\Desktop\\Code files\\CSV File\\10_benchmark_indices.csv")
print("Top 5 rows and columns of the dataset : \n",benchmark_indices.head())
print("Shape of the dataset : \n",benchmark_indices.shape)
print("Data types of the dataset : \n",benchmark_indices.dtypes)
print("Columns of the dataset : \n",benchmark_indices.columns)