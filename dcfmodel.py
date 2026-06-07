

from edgar import Company, set_identity
set_identity("con.arnold@outlook.com")

financials = Company("AMD").get_financials()
income_statement = financials.income_statement()
cashflow_statement = financials.cashflow_statement()
balance_sheet = financials.balance_sheet()


#print(income_statement)

df = income_statement.to_dataframe()
year_cols = [col for col in df.columns if col.startswith("20")]

revenue = df[(df["standard_concept"] == "Revenue") & (df["dimension"] == False)]

print(revenue[year_cols])

operating_income = df[(df["standard_concept"] == "OperatingIncomeLoss") & (df["dimension"] == False)]
print(operating_income[year_cols])

income_before_tax = df[(df["standard_concept"] == "PretaxIncomeLoss") & (df["dimension"] == False)]
print(income_before_tax[year_cols])

income_tax_expense = df[(df["standard_concept"] == "IncomeTaxes") & (df["dimension"] == False)]
print(income_tax_expense[year_cols])

shares_outstanding = df[(df["standard_concept"] == "SharesFullyDilutedAverage") & (df["dimension"] == False)]
print(shares_outstanding[year_cols])


#print(cashflow_statement)

df = cashflow_statement.to_dataframe()
year_cols = [col for col in df.columns if col.startswith("20")]

depreciation_and_amortization = df[df["label"].str.contains("Depreciation", na=False) & (df["dimension"] == False)]
print(depreciation_and_amortization[year_cols])

capex = df[(df["standard_concept"] == "CapitalExpenses") & (df["dimension"] == False) &  (df["parent_concept"].str.contains("Investing", case=False, na=False))]
print(capex[year_cols])


#print(balance_sheet)

df = balance_sheet.to_dataframe()
year_cols = [col for col in df.columns if col.startswith("20")]

current_assets = df[(df["standard_concept"] == "CurrentAssetsTotal") & (df["dimension"] == False)]
print(current_assets[year_cols])

current_liabilities = df[(df["standard_concept"] == "CurrentLiabilitiesTotal") & (df["dimension"] == False)]
print(current_liabilities[year_cols])

short_term_debt = df[(df["standard_concept"] == "ShortTermDebt") & (df["dimension"] == False)]
print(short_term_debt[year_cols])

long_term_debt = df[(df["standard_concept"] == "LongTermDebt") & (df["dimension"] == False)]
print(long_term_debt[year_cols])

cash_and_equivalents = df[(df["standard_concept"] == "CashAndMarketableSecurities") & (df["dimension"] == False)]
print(cash_and_equivalents[year_cols])

