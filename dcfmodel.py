import pandas as pd

from edgar import Company, set_identity
set_identity("con.arnold@outlook.com")
ticker = input("Enter the ticker symbol of your chosen company: ").upper()

def get_dcf_inputs(ticker):
    filings = Company(ticker).get_filings(form="10-K", amendments=False)
    results_revenue = []
    results_operating_income = []
    results_income_before_tax = []
    results_income_tax_expense = []
    results_shares_outstanding = [] 
    results_DandA = []
    results_capex = []
    results_current_assets = []
    results_current_liabilities = []
    results_short_term_debt = []
    results_long_term_debt = []
    results_cash_and_equivalents = []
    
    for filing in [filings[0], filings[1], filings[2], filings[3], filings[4], filings[5]]:
        xb = filing.xbrl()
        income_statement = xb.statements.income_statement()
        cashflow_statement = xb.statements.cashflow_statement()
        balance_sheet = xb.statements.balance_sheet()




        df = income_statement.to_dataframe()
        year_cols = [col for col in df.columns if col.startswith("20")]

        revenue = df[(df["standard_concept"] == "Revenue") & (df["dimension"] == False)]
        if not revenue.empty:
            revenue = revenue[year_cols].squeeze()
            results_revenue.append(revenue)
        
        operating_income = df[(df["standard_concept"] == "OperatingIncomeLoss") & (df["dimension"] == False)]
        if not operating_income.empty:
            operating_income = operating_income[year_cols].squeeze()
            results_operating_income.append(operating_income)

        income_before_tax = df[(df["standard_concept"] == "PretaxIncomeLoss") & (df["dimension"] == False)]
        if not income_before_tax.empty:
            income_before_tax = income_before_tax[year_cols].squeeze()
            results_income_before_tax.append(income_before_tax)

        income_tax_expense = df[(df["standard_concept"] == "IncomeTaxes") & (df["dimension"] == False)]
        if not income_tax_expense.empty:
            income_tax_expense = income_tax_expense[year_cols].squeeze()
            results_income_tax_expense.append(income_tax_expense)


        shares_outstanding = df[(df["standard_concept"] == "SharesFullyDilutedAverage") & (df["dimension"] == False)]
        if not shares_outstanding.empty:
            shares_outstanding = shares_outstanding[year_cols].squeeze()
            results_shares_outstanding.append(shares_outstanding)

        

        df = cashflow_statement.to_dataframe()
        year_cols = [col for col in df.columns if col.startswith("20")]


        depreciation_and_amortization = df[(df["label"] == "Depreciation and amortization") & (df["dimension"] == False)].head(1)
        if not depreciation_and_amortization.empty:
            depreciation_and_amortization = depreciation_and_amortization[year_cols].squeeze()
            results_DandA.append(depreciation_and_amortization)


        capex = df[(df["standard_concept"] == "CapitalExpenses") & (df["dimension"] == False) &  (df["parent_concept"].str.contains("Investing", case=False, na=False))]
        if not capex.empty:
            capex = capex[year_cols].squeeze()
            results_capex.append(capex)

        df = balance_sheet.to_dataframe()
        year_cols = [col for col in df.columns if col.startswith("20")]

        current_assets = df[(df["standard_concept"] == "CurrentAssetsTotal") & (df["dimension"] == False)]
        if not current_assets.empty:
            current_assets = current_assets[year_cols].squeeze()
            results_current_assets.append(current_assets)

        current_liabilities = df[(df["standard_concept"] == "CurrentLiabilitiesTotal") & (df["dimension"] == False)]
        if not current_liabilities.empty:
            current_liabilities = current_liabilities[year_cols].squeeze()
            results_current_liabilities.append(current_liabilities)

       

        short_term_debt = df[(df["standard_concept"] == "ShortTermDebt") & (df["dimension"] == False)]
        if not short_term_debt.empty:
            short_term_debt = short_term_debt[year_cols].squeeze()
            results_short_term_debt.append(short_term_debt)

        long_term_debt = df[(df["standard_concept"] == "LongTermDebt") & (df["dimension"] == False)]
        if not long_term_debt.empty:
            long_term_debt = long_term_debt[year_cols].squeeze()
            results_long_term_debt.append(long_term_debt)

        cash_and_equivalents = df[(df["standard_concept"] == "CashAndMarketableSecurities") & (df["dimension"] == False)]
        if not cash_and_equivalents.empty:
            cash_and_equivalents = cash_and_equivalents[year_cols].squeeze()
            results_cash_and_equivalents.append(cash_and_equivalents)
                
    
    print("\nIncome Statement data: ")
    print("\nRevenue:")
    combinded_revenue = pd.concat(results_revenue)
    combinded_revenue = combinded_revenue[~combinded_revenue.index.duplicated(keep='first')]
    print(combinded_revenue)
    print("\nOperating Income: ")
    combinded_operating_income = pd.concat(results_operating_income)
    combinded_operating_income = combinded_operating_income[~combinded_operating_income.index.duplicated(keep='first')]
    print(combinded_operating_income)
    print("\nIncome Before Tax: ")
    combinded_income_before_tax = pd.concat(results_income_before_tax)
    combinded_income_before_tax = combinded_income_before_tax[~combinded_income_before_tax.index.duplicated(keep='first')]
    print(combinded_income_before_tax)
    print("\nIncome Tax Expense: ")
    combinded_income_tax_expense = pd.concat(results_income_tax_expense)
    combinded_income_tax_expense = combinded_income_tax_expense[~combinded_income_tax_expense.index.duplicated(keep='first')]
    print(combinded_income_tax_expense)
    print("\nShares Outstanding: ")
    combinded_shares_outstanding = pd.concat(results_shares_outstanding)
    combinded_shares_outstanding = combinded_shares_outstanding[~combinded_shares_outstanding.index.duplicated(keep='first')]
    print(combinded_shares_outstanding)

    print("\nCash Flow Statement data: ")
    print("\nDepreciation and Amortization: ")
    combinded_DandA = pd.concat(results_DandA)
    combinded_DandA = combinded_DandA[~combinded_DandA.index.duplicated(keep='first')]
    print(combinded_DandA)
    print("\nCAPEX")
    combinded_capex = pd.concat(results_capex)
    combinded_capex = combinded_capex[~combinded_capex.index.duplicated(keep='first')]
    print(combinded_capex)

    print("\nBalance Sheet data:  ")
    print("\nCurrent Assets")
    combinded_current_assets = pd.concat(results_current_assets)
    combinded_current_assets = combinded_current_assets[~combinded_current_assets.index.duplicated(keep='first')]
    print(combinded_current_assets)
    print("\nCurrent Liabilities")
    combinded_current_liabilities = pd.concat(results_current_liabilities)
    combinded_current_liabilities = combinded_current_liabilities[~combinded_current_liabilities.index.duplicated(keep='first')]
    print(combinded_current_liabilities)
    print("\nShort-term Debt")
    combinded_short_term_debt = pd.concat(results_short_term_debt)
    combinded_short_term_debt = combinded_short_term_debt[~combinded_short_term_debt.index.duplicated(keep='first')]
    print(combinded_short_term_debt)
    print("\nLong-term Debt")
    combinded_long_term_debt = pd.concat(results_long_term_debt)
    combinded_long_term_debt = combinded_long_term_debt[~combinded_long_term_debt.index.duplicated(keep='first')]
    print(combinded_long_term_debt)
    print("\nCash and Cash Equivalents")
    combinded_cash_and_equivalents = pd.concat(results_cash_and_equivalents)
    combinded_cash_and_equivalents = combinded_cash_and_equivalents[~combinded_cash_and_equivalents.index.duplicated(keep='first')]
    print(combinded_cash_and_equivalents)

    return {
        "revenue": combinded_revenue,
        "operating_income": combinded_operating_income,
        "income_before_tax": combinded_income_before_tax,
        "income_tax_expense": combinded_income_tax_expense,
        "shares_outstanding": combinded_shares_outstanding,
        "depreciation_and_amortization": combinded_DandA,
        "capex": combinded_capex,
        "current_assets": combinded_current_assets,
        "current_liabilities": combinded_current_liabilities,
        "short_term_debt": combinded_short_term_debt,
        "long_term_debt": combinded_long_term_debt,
        "cash_and_equivalents": combinded_cash_and_equivalents
    }

data = get_dcf_inputs(ticker)

def summarise_ratio(series):
    mean = series.mean()
    std = series.std()
    return{
        "base": mean,
        "bear": mean - std,
        "bull": mean + std
    }




revenue = data["revenue"].sort_index()
revenue_growth = revenue.pct_change().dropna()
rev_growth = summarise_ratio(revenue_growth)
print(rev_growth)

operating_margin = (data["operating_income"] / data["revenue"]).dropna()
opm_change = summarise_ratio(operating_margin)
print(opm_change)

danda_revenue = (data["depreciation_and_amortization"] / data["revenue"]).dropna()
danda_change = summarise_ratio(danda_revenue)
print(danda_change)

capex_revenue = (data["capex"] / data["revenue"]).dropna()
capex_change = summarise_ratio(capex_revenue)
print(capex_change)

tax_rate = 0.21  # Utilising federal corporation tax rate. Effective tax rate for more volatile firms e.g. AMD caused a lot of volatility


years = 5
last_revenue = data["revenue"].sort_index().iloc[-1]
growth = rev_growth["base"]
opm = opm_change["base"]
da = danda_change["base"]
capex = capex_change["base"]
tax_rate = 0.21

projected_ufcf = []
current = last_revenue

for year in range(years):
    current = current * (1 + growth)
    ebit = current * opm
    da_addback = current * da
    capex_outflow = current * capex
    nopat = ebit * (1 - tax_rate)
    ufcf = nopat + da_addback + capex_outflow
    projected_ufcf.append(ufcf)

print(projected_ufcf)


import yfinance as yf

tax_rate = 0.21


stock = yf.Ticker(ticker)
info = stock.info

beta = info.get("beta", 1.0)
market_cap = info.get("marketCap", 0)

ten_year_yield = yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1] / 100

spx = yf.Ticker("^SP500TR").history(period="20y")["Close"]
mr = (spx.iloc[-1] / spx.iloc[0]) ** (1/20) - 1


total_debt = data["short_term_debt"].sort_index().iloc[-1] + data["long_term_debt"].sort_index().iloc[-1]

ticker = yf.Ticker(ticker)
interest_expense = ticker.income_stmt.loc["Interest Expense"].iloc[0]
print(interest_expense)

cost_of_equity = ten_year_yield + beta * (mr - ten_year_yield)
cost_of_debt_pretax = interest_expense / total_debt
cost_of_debt_aftertax = cost_of_debt_pretax * (1 - (tax_rate))
equity_weight = market_cap / (market_cap + total_debt)
debt_weight = total_debt / (market_cap + total_debt)
wacc = (cost_of_equity * equity_weight) + (cost_of_debt_aftertax * debt_weight)
print(wacc * 100)













    #print(cashflow_statement)




    #print(balance_sheet)



   

   # return {
    #"Revenue": revenue,
    #"Operating Income": operating_income,
    #"Income Before Tax": income_before_tax,
    #"Income Tax Expense": income_tax_expense,
    #"Shares Outstanding": shares_outstanding,
   # "Depreciation and Amortization": depreciation_and_amortization,
    #"Capital Expenditures": capex,
    #"Current Assets": current_assets,
    #"Current Liabilities": current_liabilities,
    #"Short-Term Debt": short_term_debt,
    #"Long-Term Debt": long_term_debt,
    #"Cash and Equivalents": cash_and_equivalents
    #}

#result = get_dcf_inputs(ticker)
#print(results["Revenue"])


#filing = Company(ticker).get_filings(form="10-K")[2]



#xb = filing.xbrl()
#income = xb.statements.income_statement()
#df = income.to_dataframe()
#print(df.columns.tolist())



#print(filing.statements)

#income = filing.statements[3]
#print(type(income))
#print(dir(income))


