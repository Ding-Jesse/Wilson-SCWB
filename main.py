import os
from src.scwb_calculator import SCWBCalculator

def main():
    print("==================================================")
    print("   Strong Column Weak Beam (SCWB) Checker Tool    ")
    print("==================================================")
    
    # Initialize the calculator
    calculator = SCWBCalculator(factor=1.2)
    
    # Define path to data
    data_path = os.path.join("data", "sample_data.csv")
    
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        return

    print(f"Processing data from: {data_path}...\n")
    
    # Process the data
    results = calculator.process_csv(data_path)
    
    if results is not None:
        # Display results
        print(results.to_string(index=False))
        
        # Save results
        output_path = os.path.join("data", "results.csv")
        results.to_csv(output_path, index=False)
        print(f"\nResults saved to: {output_path}")
        
        # Summary
        safe_count = results['is_safe'].sum()
        total_count = len(results)
        print(f"\nSummary: {safe_count}/{total_count} joints passed the SCWB check.")
    else:
        print("Failed to process data.")

if __name__ == "__main__":
    main()
