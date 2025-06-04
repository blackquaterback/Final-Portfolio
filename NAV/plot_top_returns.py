import pandas as pd
import matplotlib.pyplot as plt
import os

def create_bar_plot(data, sheet_name, output_dir):
    # Convert percentage strings to float values
    data.iloc[:, 3] = data.iloc[:, 3].str.rstrip('%').astype(float)
    
    # Create figure with larger size
    plt.figure(figsize=(15, 8))
    
    # Create bar plot
    bars = plt.bar(range(len(data)), data.iloc[:, 3])
    
    # Customize the plot
    plt.title(f'Top Performers - {sheet_name}', fontsize=14, pad=20)
    plt.xlabel('Schemes', fontsize=12)
    plt.ylabel('Returns (%)', fontsize=12)
    
    # Rotate x-axis labels for better readability
    plt.xticks(range(len(data)), data.iloc[:, 2], rotation=45, ha='right')
    
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%',
                ha='center', va='bottom')
    
    # Add grid for better readability
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the plot
    output_file = os.path.join(output_dir, f'{sheet_name.replace(" ", "_")}.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Created plot for {sheet_name}")

def main():
    # Create output directory if it doesn't exist
    output_dir = 'return_plots'
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the Excel file
    excel_file = 'nav_returns.xlsx'
    
    # Sheet indices to plot (3,5,7,9,11,13,15)
    # Excel sheet indices are 0-based, so we subtract 1
    sheet_indices = [2, 4, 6, 8, 10, 12, 14]
    
    try:
        # Read all sheets
        xl = pd.ExcelFile(excel_file)
        sheet_names = xl.sheet_names
        
        print("Processing sheets...")
        
        # Create plots for specified sheets
        for idx in sheet_indices:
            if idx < len(sheet_names):
                sheet_name = sheet_names[idx]
                print(f"\nProcessing sheet: {sheet_name}")
                
                # Read the sheet
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                
                # Create and save the plot
                create_bar_plot(df, sheet_name, output_dir)
            else:
                print(f"Warning: Sheet index {idx+1} does not exist in the Excel file")
        
        print(f"\nAll plots have been saved to the '{output_dir}' directory")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file '{excel_file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 