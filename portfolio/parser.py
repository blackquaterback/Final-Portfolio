from core.FundPortfolioParser import FundPortfolioParser
from portfolio.eparse import * 
import pandas as pd

class ParagParikhParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Parag Parikh Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_parag_parikh(sheet_df, fund_name, self.full_path)

class ICICIParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="ICICI Prudential Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_icici(sheet_df, fund_name, self.full_path)

class MiraeParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Mirae Asset Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_mirae(sheet_df, fund_name, self.full_path)

class QuantParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Quant Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_quant(sheet_df, fund_name, self.full_path)

class SBINParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="SBI Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_sbin(sheet_df, fund_name, self.full_path)

class NipponParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Nippon Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_nippon(sheet_df, fund_name, self.full_path)

class AxisParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Axis Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_axis(sheet_df, fund_name, self.full_path)

class KotakParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Kotak Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_kotak(sheet_df, fund_name, self.full_path)

class HDFCParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="HDFC Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_hdfc(sheet_df, fund_name, self.full_path)

class BankOfIndiaParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Bank of India Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_bankofindia(sheet_df, fund_name, self.full_path)

class CaneraRobecoParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Canera Robeco Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_canerarobeco(sheet_df, fund_name, self.full_path)

class DSPParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="DSP Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_dsp(sheet_df, fund_name, self.full_path)

class InvescoParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Invesco Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_invesco(sheet_df, fund_name, self.full_path)

class JMFinancialParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="JM Financial Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_jmfinancial(sheet_df, fund_name, self.full_path)

class LICParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="LIC Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_lic(sheet_df, fund_name, self.full_path)

class MotilalOswalParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Motilal Oswal Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_motilaloswal(sheet_df, fund_name, self.full_path)

class NaviParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Navi Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_navi(sheet_df, fund_name, self.full_path)

class OldBridgeCapitalParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Old Bridge Capital Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_oldbridgecapital(sheet_df, fund_name, self.full_path)

