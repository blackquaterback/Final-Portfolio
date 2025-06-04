import pandas as pd
import matplotlib.pyplot as plt
import os
import re
from datetime import datetime, timedelta

def read_mf_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    data_start_index = next(
        (i for i, line in enumerate(lines) if re.match(r'\d{6}', line.strip().split(';')[0])),
        None
    )
    
    if data_start_index is None:
        return pd.DataFrame()
    
    data_lines = lines[data_start_index:]
    data = []
    
    for line in data_lines:
        line = line.strip()
        if line:
            parts = line.split(';')
            if len(parts) >= 8:
                isin = parts[2].strip()
                if isin and len(isin) >= 10:
                    data.append(parts)
    
    columns = [
        "Scheme Code", "Scheme Name", "ISIN Div Payout/ISIN Growth", "ISIN Div Reinvestment", 
        "Net Asset Value", "Repurchase Price", "Sale Price", "Date"
    ]
    
    df = pd.DataFrame(data, columns=columns)
    
    df["Scheme Code"] = pd.to_numeric(df["Scheme Code"], errors='coerce')
    df["Net Asset Value"] = pd.to_numeric(df["Net Asset Value"], errors='coerce')
    df["Repurchase Price"] = pd.to_numeric(df["Repurchase Price"], errors='coerce')
    df["Sale Price"] = pd.to_numeric(df["Sale Price"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    
    df = df[df['ISIN Div Payout/ISIN Growth'].str.len() >= 10].copy()
    
    return df.dropna(subset=["Scheme Code", "Net Asset Value", "Date", "ISIN Div Payout/ISIN Growth"])

def extract_amc_name(scheme_name):
    if scheme_name.startswith("Parag Parikh"):
        return "Parag Parikh"
    elif scheme_name.startswith("Aditya Birla Sun"):
        return "Aditya Birla Sun"
    else:
        return scheme_name.split(" ")[0]

def calculate_return(start_nav, end_nav):
    if start_nav == 0 or pd.isna(start_nav) or pd.isna(end_nav):
        return None
    return ((end_nav - start_nav) / start_nav) * 100

def plot_fund_timeseries(fund_data, scheme_name, output_dir):
    periods = {
        '1W': 7,
        '1M': 30,
        '1Y': 365,
        '3Y': 3 * 365,
        '5Y': 5 * 365,
        'Total': None
    }
    
    plt.figure(figsize=(15, 10))
    fund_data = fund_data.sort_values('Date')
    
    # Plot the full time series
    plt.plot(fund_data['Date'], fund_data['Net Asset Value'], label='NAV', linewidth=2)
    
    # Calculate and display returns for each period
    latest_nav = fund_data['Net Asset Value'].iloc[-1]
    latest_date = fund_data['Date'].iloc[-1]
    returns_text = []
    
    for period_name, days in periods.items():
        if days is None:
            # Total return
            first_nav = fund_data['Net Asset Value'].iloc[0]
            returns = calculate_return(first_nav, latest_nav)
        else:
            # Period-specific return
            past_date = latest_date - timedelta(days=days)
            past_data = fund_data[fund_data['Date'] <= past_date]
            if not past_data.empty:
                past_nav = past_data['Net Asset Value'].iloc[-1]
                returns = calculate_return(past_nav, latest_nav)
            else:
                returns = None
        
        if returns is not None:
            returns_text.append(f"{period_name}: {returns:.2f}%")
    
    # Add returns text to plot
    plt.text(0.02, 0.98, '\n'.join(returns_text),
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.title(f"{scheme_name}\nNAV Progression and Returns", fontsize=12, pad=20)
    plt.xlabel('Date')
    plt.ylabel('NAV')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Create safe filename
    safe_name = "".join(x for x in scheme_name if x.isalnum() or x in (' ', '-', '_'))[:100]
    plt.savefig(os.path.join(output_dir, f"{safe_name}.png"), dpi=300, bbox_inches='tight')
    plt.close()

def process_file(file_path, base_output_dir):
    print(f"\nProcessing file: {file_path}")
    df = read_mf_data(file_path)
    
    if df.empty:
        print("No valid data found in file")
        return
    
    # Add AMC column
    df['AMC'] = df['Scheme Name'].apply(extract_amc_name)
    
    # Process each AMC separately
    for amc in df['AMC'].unique():
        print(f"\nProcessing AMC: {amc}")
        
        # Create AMC directory
        amc_dir = os.path.join(base_output_dir, amc)
        os.makedirs(amc_dir, exist_ok=True)
        
        # Get all funds for this AMC
        amc_data = df[df['AMC'] == amc]
        
        # Process each fund
        for scheme_code in amc_data['Scheme Code'].unique():
            fund_data = amc_data[amc_data['Scheme Code'] == scheme_code].copy()
            scheme_name = fund_data['Scheme Name'].iloc[0]
            print(f"Plotting {scheme_name}")
            
            plot_fund_timeseries(fund_data, scheme_name, amc_dir)

def main():
    start_time = datetime.now()
    print(f"Processing started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    directory_path = "C:/Users/SAURABH/Desktop/Portfolio/nav"
    output_dir = os.path.join(directory_path, "fund_plots_by_amc")
    
    # Process each txt file
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            process_file(file_path, output_dir)
    
    end_time = datetime.now()
    print(f"\nTotal processing time: {end_time - start_time}")
    print(f"\nPlots have been saved to: {output_dir}")

if __name__ == "__main__":
    main() 