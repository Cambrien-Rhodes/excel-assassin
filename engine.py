#Import necessary libraries

import pandas as pd
import io

#This is where the work is done.

def run_assassin(uploaded_file, threshold):
    uploaded_file.seek(0)

    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')
    
    except Exception:

        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file)

    required_col = "Stock_Level"
    if required_col not in df.columns:
        alternatives = ["Quantity", "Qty On Hand", "Stock", "Current_Stock"]
        found = False
        for alt in alternatives:
            if alt in df.columns:
                df.rename(columns={alt: required_col}, inplace=True)
                found = True
                break

        if not found:
            raise ValueError(f"Missing required column: {required_col}")

    results = df[df["Stock_Level"] < threshold]

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        results.to_excel(writer, index=False)

    output.seek(0)
    return output
