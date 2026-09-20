import pandas as pd

# Load the CSV file
input_file = "submission_ensemble_07.csv"
output_file = "submission_ensemble_07_no14.csv"

# Read the CSV into a DataFrame
df = pd.read_csv(input_file, header=None, names=["id", "value"])

# Filter out rows starting with "TYM0IJW004"
df_filtered = df[~df["id"].str.startswith("TYM0IJW004")]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv(output_file, index=False, header=False)

print(f"Filtered data saved to {output_file}")