import pandas as pd

class SCWBCalculator:
    """
    A calculator for checking the Strong Column Weak Beam (SCWB) condition.
    
    The SCWB concept ensures that during a seismic event, plastic hinges form in the beams
    rather than the columns, preventing catastrophic collapse.
    
    Standard Check: Sum(M_c) >= 1.2 * Sum(M_b)
    where:
        M_c = Nominal moment capacity of columns at the joint
        M_b = Nominal moment capacity of beams at the joint
    """
    
    def __init__(self, factor=1.2):
        """
        Initialize the calculator.
        
        Args:
            factor (float): The safety factor for the check. Default is 1.2 (ACI 318).
        """
        self.factor = factor

    def check_joint(self, sum_mc, sum_mb):
        """
        Check a single joint for SCWB compliance.
        
        Args:
            sum_mc (float): Sum of column moment capacities.
            sum_mb (float): Sum of beam moment capacities.
            
        Returns:
            dict: A dictionary containing the check result and details.
        """
        required_mc = self.factor * sum_mb
        is_safe = sum_mc >= required_mc
        ratio = sum_mc / sum_mb if sum_mb != 0 else float('inf')
        
        return {
            "sum_mc": sum_mc,
            "sum_mb": sum_mb,
            "required_mc": required_mc,
            "ratio": ratio,
            "is_safe": is_safe,
            "message": "Strong Column Weak Beam Satisfied" if is_safe else "WARNING: Weak Column Detected"
        }

    def process_csv(self, file_path):
        """
        Process a CSV file containing joint data.
        
        Expected CSV columns:
            - joint_id
            - sum_mc
            - sum_mb
            
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            pd.DataFrame: The original data with check results appended.
        """
        try:
            df = pd.read_csv(file_path)
            
            results = []
            for _, row in df.iterrows():
                res = self.check_joint(row['sum_mc'], row['sum_mb'])
                results.append(res)
                
            results_df = pd.DataFrame(results)
            final_df = pd.concat([df, results_df[['ratio', 'is_safe', 'message']]], axis=1)
            
            return final_df
        except Exception as e:
            print(f"Error processing file: {e}")
            return None
