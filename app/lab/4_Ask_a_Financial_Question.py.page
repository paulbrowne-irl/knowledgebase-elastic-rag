import streamlit as st

from elasticsearch import Elasticsearch
#import eland as ed

from importlib import reload

import settings.config as config
import pages.app_sidebar as app_sidebar
from service import rag_factory as rag_factory
import logging


@st.cache_data(show_spinner=True)
def get_unique_cols():
    
    values =[
        'AccountStatus',
        'Accruals_OtherCreditors',
        'AddbackDepreciation_Amortisation',
        'AdminCharge',
        'Amortisation',
        'Bank_Cash',
        'BankOverdraftFacilityLimitforProjectedYears',
        'BankOverdraftFacilityLimitinProjectedYears',
        'Capex_minus_Intangible',
        'Capex_minus_Tangible',
        'CapitalExpenditure',
        'CapitalisedRD000s',
        'CashavailableafterServicingFinancingObligations',
        'CashavailableforServicingFinancingObligations',
        'CashFlowStatementFortheyearended',
        'ClosingCashInclFacilitiesi.e.availablecash',
        'ConnectedParties_InterCompanyLoans',
        'CostofSales',
        'CurrentAssets',
        'CurrentLiabilities',
        'Depreciation',
        'DirectLabour',
        'Directors_ShareholdersLoans',
        'Directorsloans',
        'DistributionSalesofOtherCosProduct',
        'Dividends',
        'DividendsPaidtoEI',
        'EIEquityAssistanceThisapplicationonly',
        'EIgrant',
        'EIGrantLiabilityThisapplicationonly',
        'EIrepayableadvance',
        'Financedby',
        'FixedAssets',
        'GrantAmortisationThisapplicationonly',
        'GrossProfit_Loss',
        'Group',
        'IDfacility',
        'IndirectLabourexcludingRDSalaries',
        'Intangible',
        'IntangibleassetExclCapitalisedRD',
        'Interest_DividendsReceivable',
        'InterestPayable',
        'Inventory',
        'Investments',
        'InvoiceDiscountingBalance',
        'InvoicediscountingProjectedYearEndBalance',
        'InvoicediscountingYEBalance',
        'Leases',
        'Leasing',
        'Liabilities1Year',
        'LongTermLoans',
        'NetAssets',
        'NetClosingCashExclShortTermFacilities',
        'NetCurrentAssets',
        'NetMovementinCash',
        'NetProfit_Loss',
        'Newfunding',
        'NewMachinery_otherCapex',
        'No.ofGlobalEmployeesYEinclIrishemployment',
        'No.ofGlobalRDEmployeesYE',
        'No.ofIrishBasedEmployeesYE',
        'No.ofIrishBasedRDEmployeesYE',
        'Non_minus_OperatingExpenses_Gains',
        'OpeningCashBalance_minus_includesFacilities',
        'OperatingCashInflow_Outflow',
        'OperatingExpenditure',
        'OperatingProfit_Loss_minus_EBITDA',
        'Ordequity',
        'OrdinarySharesSharePremium',
        'Other',
        'OtherCostofGoodsSold',
        'OtherDividendsPaid',
        'OtherEquityInvestment_Divestment',
        'Otherfinancingrequirements',
        'OtherLongTermLiabilities',
        'OtherOperatingExpenses_Gains',
        'OtherRDexpenditure',
        'Overdraft',
        'OverdraftFacility',
        'OwnProduct_ServiceProducedAbroadsoldAbroad',
        'OwnProduct_ServiceProducedinIrelandExported',
        'OwnProduct_ServiceProducedSoldinIreland',
        'PreferenceShares',
        'Preferredequity',
        'Prepayments_OtherDebtors',
        'Profit_LossbeforeTax',
        'ProfitRetainedfortheYear',
        'PromotersEquityInvestment_Divestment',
        'Provisions_Grants_OtherReserves',
        'Purchases',
        'RDExpenditure',
        'RDSalaries',
        'RemittedProfitstoIrelandFromForeignSubsidiary',
        'RetainedEarnings',
        'Sales',
        'SellingGeneralAdminExpenses',
        'Servicingoffunding',
        'ShareholdersFunds',
        'Shorttermloans_Leasing',
        'ShortTermloans_Leasing1year',
        'Site_BuildingsModifications',
        'Site_BuildingsPurchase',
        'Stocks',
        'TangibleFixedAssets',
        'Tax',
        'Total',
        'TotalCurrentAssets',
        'TotalCurrentLiabilities',
        'TotalFixedAssets',
        'Totalfundinginjection',
        'TotalIrishLabourCosts000s',
        'TotalLiabilities1Year',
        'Totalobligations',
        'TotalSales',
        'TradeCreditors',
        'TradeDebtors',
        'VAT_PAYE_PRSIpaid_Receivedinyear',
        'WorkingCapitalIncrease_Decrease'
        ]
    return values



#@st.cache_data(show_spinner=True)
def get_data(filter,max_docs):

    logging.debug("Running Data Query filter = "+str(filter))

    # Make the connection
    es = Elasticsearch(config.read("ES_URL"))
    #es_info = es.info()

    #Get  main table    
    sef_financials = ed.DataFrame(es, config.read("ES_INDEX_FINANCIALS"))
    sef_financials = sef_financials[['Source','Row','Col',"Table","Value"]]

    #filter main table
    if(len(filter)>0):
        #sef_financials = sef_financials.query(filter)
        sef_financials=sef_financials[sef_financials['Row'].isin(filter)]

    #sanity check filter
    print (f'Filtering to {max_docs} lines')
    sef_financials = sef_financials.head(max_docs)

    #change to pandas
    pd_financials =  ed.eland_to_pandas(sef_financials)

    #Change Data frame data
    pd_financials['Value'] = pd_financials['Value'].astype('float64',errors='ignore')
    pd_financials['Col'] = pd_financials['Col'].str[-2:]
    pd_financials=pd_financials.loc[pd_financials['Col'].isin(["16","17","18","19","20","21","22","23"])]


    return pd_financials


base_colours= ["#fd0", "#f0f", "#04f"]

#############
# Main UI

#Window setup
st.title('Show me the numbers')

#Fields on Sidebar
reload(app_sidebar)


with st.form('my_form'):



    #input elements
    filter = st.multiselect("Filter",get_unique_cols())

    max_docs = st.slider('How many lines docs do you want to see?', 1, 1000,100)

   
    submitted = st.form_submit_button('Submit')


    # Get the dataframes 
    sef_financials = get_data(filter,max_docs)
    graph_financials = sef_financials[['Col','Row','Value']]
    
    #pivot this
    # gf1=graph_financials.pivot_table( columns=['Row','Col'], values='Value', aggfunc='sum')
    pivotf=graph_financials.pivot_table( index=['Row'], columns=['Col'],values='Value', aggfunc='sum',fill_value=0).reset_index()
    
    # Tabs setup
    tab_table,tab_scatter, tab_pivot, tab_bar, = st.tabs(["Table","Scatter", "Summary","Bar"])

    if submitted:
        
        #Setup tabs
        with tab_table:

            # magic output
            st.dataframe(sef_financials,hide_index=True,use_container_width=True)

        with tab_scatter:
            st.header('Graph')
            st.scatter_chart(graph_financials,x="Col",y="Value",use_container_width=True)

        with tab_pivot:
            st.dataframe(pivotf,hide_index=True,use_container_width=True)

        with tab_bar:
            st.header('Total')
            st.bar_chart(pivotf,x="Row",y=["17","18","19","20","21","22","23"],use_container_width=True)


        

            # check we have a link
            #if not document_search.startswith('All'):
            #st.warning('Elastic filtering not implented yet!', icon='⚠')

    