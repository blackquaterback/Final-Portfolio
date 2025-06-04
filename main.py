import os
from portfolio.parser import * #this will import all the parsers from the parser module

if __name__ == "__main__":
    # set the base dir
    base_dir = os.path.join(os.getcwd(), "data")  # You can modify this path as needed

    # List of AMC names
    amc_names = [
        "360 One Asset Management", "Aditya Birla Sun Life Mutual Fund", "Axis Mutual Fund", 
        "Bandhan Mutual Fund", "Bank of India Mutual Fund", "Baroda BNP Paribas Mutual Fund", 
        "Canara Robeco Mutual Fund", "DSP Mutual Fund", "Edelweiss Mutual Fund", "Franklin Templeton India", 
        "Groww Mutual Fund", "HDFC Mutual Fund", "Helios Mutual Fund", "HSBC Mutual Fund", 
        "ICICI Prudential Mutual Fund", "Invesco Mutual Fund", "ITI Mutual Fund", "JM Financial Mutual Fund", 
        "Kotak Mutual Fund", "LIC Mutual Fund", "Mahindra Manulife Mutual Fund", "Mirae Asset Mutual Fund", 
        "Motilal Oswal Mutual Fund", "Navi Mutual Fund", "Nippon India Mutual Fund", "NJ Mutual Fund", 
        "PGIM India Mutual Fund", "PPFAS Mutual Fund", "Quant Mutual Fund", "Quantum Mutual Fund", 
        "SBI Mutual Fund", "Shriram Mutual Fund", "Sundaram Mutual Fund", "Tata Mutual Fund", 
        "Trust Mutual Fund", "Union Mutual Fund", "UTI Mutual Fund", "WhiteOak Mutual Fund", 
        "Zerodha Fund House"
    ]

    # Create a directory for each AMC if it doesn't exist
    for amc in amc_names:
        amc_dir = os.path.join(base_dir, amc)
        os.makedirs(amc_dir, exist_ok=True)
        
        # Process each AMC based on its name
        match amc:
            case "PPFAS Mutual Fund":
                parser = ParagParikhParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "HDFC Mutual Fund":
                parser = HDFCParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "ICICI Prudential Mutual Fund":
                parser = ICICIParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Axis Mutual Fund":
                parser = AxisParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Mirae Asset Mutual Fund":
                parser = MiraeParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Nippon India Mutual Fund":
                parser = NipponParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Quant Mutual Fund":
                parser = QuantParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "SBI Mutual Fund":
                parser = SBINParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Kotak Mutual Fund":
                parser = KotakParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Bank of India Mutual Fund":
                parser = BankOfIndiaParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Canara Robeco Mutual Fund":
                parser = CaneraRobecoParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "DSP Mutual Fund":
                parser = DSPParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Invesco Mutual Fund":
                parser = InvescoParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "JM Financial Mutual Fund":
                parser = JMFinancialParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "LIC Mutual Fund":
                parser = LICParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Motilal Oswal Mutual Fund":
                parser = MotilalOswalParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case "Navi Mutual Fund":
                parser = NaviParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")

            case _:
                print(f"No parser implemented yet for {amc}")

    print("Processing complete!")



    # set the base dir
    base_dir = "/Users/njp60/Documents/code/mutualfundbackend/funddata/data2/"

    # List of AMC names
    amc_names = [
        "360 One Asset Management", "Aditya Birla Sun Life Mutual Fund", "Axis Mutual Fund", 
        "Bandhan Mutual Fund", "Bank of India Mutual Fund", "Baroda BNP Paribas Mutual Fund", 
        "Canara Robeco Mutual Fund", "DSP Mutual Fund", "Edelweiss Mutual Fund", "Franklin Templeton India", 
        "Groww Mutual Fund", "HDFC Mutual Fund", "Helios Mutual Fund", "HSBC Mutual Fund", 
        "ICICI Prudential Mutual Fund", "Invesco Mutual Fund", "ITI Mutual Fund", "JM Financial Mutual Fund", 
        "Kotak Mutual Fund", "LIC Mutual Fund", "Mahindra Manulife Mutual Fund", "Mirae Asset Mutual Fund", 
        "Motilal Oswal Mutual Fund", "Navi Mutual Fund", "Nippon India Mutual Fund", "NJ Mutual Fund", 
        "PGIM India Mutual Fund", "PPFAS Mutual Fund", "Quant Mutual Fund", "Quantum Mutual Fund", 
        "SBI Mutual Fund", "Shriram Mutual Fund", "Sundaram Mutual Fund", "Tata Mutual Fund", 
        "Trust Mutual Fund", "Union Mutual Fund", "UTI Mutual Fund", "WhiteOak Mutual Fund", 
        "Zerodha Fund House"
    ]

    # Create a directory for each AMC
    for amc in amc_names:
        
        match amc:

    
            case "Parag Parikh Mutual Fund":
            # Process Parag Parikh Mutual Fund
                amc_dir = os.path.join(base_dir, amc)
                parser = ParagParikhParser(amc_dir)
                output_df = parser.process()
                output_df.to_excel(os.path.join(amc_dir, "output.xlsx"), index=False)
                print(f"Processed {amc} and saved to {amc_dir}/output.xlsx")


            case "HDFC Mutual Fund":
            # Process Parag Parikh Mutual Fund
                amc_dir = os.path.join(base_dir, amc)

                #create HDFC parser 
              
            case "ICICI Prudential Mutual Fund":
            # Process Parag Parikh Mutual Fund
                amc_dir = os.path.join(base_dir, amc)

                #create ICICI parser 
            case "ICICI Prudential Mutual Fund":
            # Process Parag Parikh Mutual Fund
                amc_dir = os.path.join(base_dir, amc)

                #create ICICI parser 


        
              
