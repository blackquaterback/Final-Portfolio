from core.FundPortfolioParser import FundPortfolioParser
from portfolio.eparse  import clean_parag_parikh


# start creating parser # for Parag Parikh Mutual Fund by overriding the methods in FundPortfolioParser with necessary edits


class ParagParikhParser(FundPortfolioParser):
    def __init__(self, datadir):
        super().__init__(datadir, amc_name="Parag Parikh Mutual Fund")

    def _read_index_sheet(self):
        df = pd.read_excel(self.full_path, sheet_name="Index", dtype=str)
        return dict(zip(df['Short Name'], df['Scheme Name']))

    def _clean_sheet(self, sheet_df, fund_name):
        return clean_parag_parikh(sheet_df, fund_name, self.full_path)


