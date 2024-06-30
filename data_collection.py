import yfinance as yf
from llama_index import SimpleDirectoryReader
from llama_index.core.tools import FunctionTool

def fetch_historical_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data.to_dict('list')

def fetch_financial_news_from_directory(directory_path):
    documents = SimpleDirectoryReader(directory_path).load_data()
    return documents

def fetch_financial_reports_from_directory(directory_path):
    documents = SimpleDirectoryReader(directory_path).load_data()
    return documents

stock_data_tool = FunctionTool.from_defaults(fetch_historical_stock_data, name="StockDataTool", description="Fetch historical stock data for a given ticker symbol")
news_data_tool = FunctionTool.from_defaults(fetch_financial_news_from_directory, name="NewsDataTool", description="Fetch financial news from a directory")
reports_data_tool = FunctionTool.from_defaults(fetch_financial_reports_from_directory, name="ReportsDataTool", description="Fetch financial reports from a directory")
