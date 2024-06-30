from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
from data_collection import stock_data_tool, news_data_tool, reports_data_tool
from sentiment_analysis import sentiment_analysis_tool
from strategy_generation import strategy_generation_tool
from advisory import advice_tool, market_analysis_tool, industry_trends_tool, financial_ratios_tool, portfolio_management_tool
from portfolio_optimization import portfolio_optimization_tool
from risk_assessment import risk_assessment_tool
from trading import trading_tool
from user_interface import user_interface_tool
from concurrent.futures import ThreadPoolExecutor
from config import OPENAI_API_KEY
import pandas as pd


llm = OpenAI(model="gpt-3.5-turbo-0613", api_key=OPENAI_API_KEY)


# Initialize the agent with all tools
tools = [
    stock_data_tool,
    news_data_tool,
    reports_data_tool,
    sentiment_analysis_tool,
    strategy_generation_tool,
    advice_tool,
    market_analysis_tool,
    industry_trends_tool,
    financial_ratios_tool,
    portfolio_management_tool,
    portfolio_optimization_tool,
    risk_assessment_tool,
    trading_tool,
    user_interface_tool,
]


agent = OpenAIAgent.from_tools(tools, llm=llm, verbose=True)


def orchestrate():
    # Step 1: Gather User Input
    customer_data = agent.call("UserInterfaceTool")

    # Step 2: Data Collection
    with ThreadPoolExecutor() as executor:
        stock_data_future = executor.submit(agent.call, "StockDataTool", ticker="AAPL", start_date="2022-01-01", end_date="2022-12-31")
        financial_news_future = executor.submit(agent.call, "NewsDataTool", directory_path="./news_data")
        financial_reports_future = executor.submit(agent.call, "ReportsDataTool", directory_path="./reports_data")
    
    stock_data = stock_data_future.result()
    financial_news = financial_news_future.result()
    financial_reports = financial_reports_future.result()

    # Step 3: Sentiment Analysis
    news_texts = [news["text"] for news in financial_news]
    sentiment_analysis_results = agent.call("SentimentAnalysisTool", news_texts)

    # Step 4: Strategy Generation
    investment_strategy = agent.call("StrategyGenerationTool", stock_data, sentiment_analysis_results, customer_data["risk_tolerance"])

    # Step 5: Enhanced Analysis
    market_analysis = agent.call("MarketAnalysisTool", stock_data)
    industry_trends = agent.call("IndustryTrendsTool", "AAPL")
    financial_ratios = agent.call("FinancialRatiosTool", stock_data)
    portfolio_management = agent.call("PortfolioManagementTool", customer_data["risk_tolerance"])

    # Step 6: Advisory
    financial_advice = agent.call("AdvisoryTool", customer_data, investment_strategy, market_analysis, industry_trends, financial_ratios, portfolio_management)

    # Step 7: Portfolio Optimization
    df = pd.DataFrame(stock_data)  # Convert stock_data to DataFrame
    expected_returns = df['Close'].pct_change().mean() * 252  # Annualized returns (simplified example)
    covariances = df['Close'].pct_change().cov() * 252         # Annualized covariances (simplified example)
    optimal_allocation = agent.call("PortfolioOptimizationTool", expected_returns, covariances, customer_data["risk_tolerance"])
    
    # Step 8: Risk Assessment
    risk_assessment_results = agent.call("RiskAssessmentTool", stock_data)
    

    # Step 9: Trading (Conceptual)
    for ticker, weight in optimal_allocation.items():
        action = "BUY" if weight > 0 else "SELL"  # Simplified logic
        quantity = weight * customer_data["investment_amount"]  
        agent.call("TradingTool", ticker, action, quantity) 

    # Output the results
    print("Financial Advice:", financial_advice)
    print("Strategy Explanation:", investment_strategy)
    print("Optimal Allocation:", optimal_allocation)
    print("Risk Assessment Results:", risk_assessment_results)


if __name__ == "__main__":
    orchestrate()
