# Multi-Agent Financial Advisory System with LlamaIndex and OpenAI

This project demonstrates a sophisticated multi-agent system designed to provide comprehensive financial advisory services using LlamaIndex and OpenAI. The system leverages multiple intelligent agents, each specializing in a different aspect of financial analysis and decision-making.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Agents](#agents)
- [Tools](#tools)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Project Overview

This prototype simulates a financial advisory platform where various agents collaborate to collect data, analyze market trends, generate investment strategies, assess risk, and provide personalized financial advice. The system aims to showcase the potential of multi-agent systems in the financial domain, offering a glimpse into the future of automated financial advisory services.

## Features

- **Multi-Agent Architecture:** Employs multiple specialized agents, each handling a specific task in the financial advisory process.
- **LlamaIndex Integration:** Utilizes LlamaIndex for efficient data indexing, retrieval, and knowledge management.
- **OpenAI Model:** Leverages the power of OpenAI's language models for natural language processing and generation of intelligent responses.
- **Portfolio Optimization:** Optimizes portfolio allocation based on risk tolerance and expected returns.
- **Risk Assessment:** Assesses the risk profile of investment options using various metrics.
- **Trading Simulation:** Simulates trade execution based on generated investment strategies (conceptual).
- **User Interface Interaction:** Gathers user input and preferences (conceptual).
- **Market Analysis:** Analyzes market trends and sentiment to inform investment decisions.
- **Industry Trend Analysis:** Assesses trends within specific industries.
- **Financial Ratio Calculation:** Calculates and interprets key financial ratios.
- **Portfolio Management Advice:** Provides personalized portfolio management recommendations.
- **Investment Strategy Generation:** Generates investment strategies based on comprehensive analysis.
- **Sentiment Analysis:** Analyzes news and financial reports to gauge market sentiment.
- **Explainability:** Offers explanations for the generated investment strategies.
- **MLflow Tracking:** Logs model parameters and metrics for experiment tracking and reproducibility.

## Architecture

The system consists of the following key components:

- **Agents:** Each agent specializes in a specific task, such as data collection, sentiment analysis, strategy generation, risk assessment, portfolio optimization, trading, and user interface interaction.
- **Tools:** Agents utilize various tools for data retrieval, analysis, and strategy generation, including LlamaIndex tools, OpenAI's API, and custom-built functions.
- **Orchestrator:** The orchestrator manages the interactions between agents, coordinating the flow of information and tasks to achieve the overall financial advisory objective.

## Agents

- **Data Collection Agent:** Fetches historical stock data, financial news, and reports.
- **Sentiment Analysis Agent:** Analyzes sentiment in news articles and reports.
- **Strategy Generation Agent:** Generates investment strategies based on analysis.
- **Advisory Agent:** Provides personalized financial advice.
- **Market Analysis Agent:** Analyzes market trends.
- **Industry Trends Agent:** Assesses industry-specific trends.
- **Financial Ratios Agent:** Calculates and interprets financial ratios.
- **Portfolio Management Agent:** Provides portfolio management advice.
- **Risk Assessment Agent:** Assesses the risk profile of investments.
- **Trading Agent:** Executes buy/sell orders (conceptual).
- **User Interface Agent:** Gathers user input and presents information (conceptual).

## Tools

- **LlamaIndex Tools:**  Various tools for data indexing, retrieval, and knowledge management.
- **OpenAI API:** For natural language processing and generation.
- **Custom Functions:** Python functions for data analysis, risk assessment, portfolio optimization, etc.

## Getting Started

### Installation

1. **Clone the Repository:** 
   ```bash
   git clone https://github.com/dhrumilvthakkar/financial-advisor.git
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Azure Cognitive Services:**
   - Create an Azure account and obtain an API key for the Text Analytics service.
   - Set the following environment variables:
     - `AZURE_KEY`: Your Azure Text Analytics API key.
     - `AZURE_ENDPOINT`: Your Azure Text Analytics endpoint URL.

2. **OpenAI API:**
   - Obtain an API key from OpenAI.
   - Set the following environment variable:
     - `OPENAI_API_KEY`: Your OpenAI API key.

3. **MLflow Tracking Server:**
   - (Optional, but recommended) Set up an MLflow tracking server (e.g., using `mlflow server`) to log and track experiments.
   - Set the following environment variable:
     - `MLFLOW_TRACKING_URI`: The URI of your MLflow tracking server. If not using a server, set it to `sqlite:///mlflow.db` to store logs locally.

### Usage

1. **Prepare Data:**
   - Create two folders: `news_data` and `reports_data`.
   - Place relevant financial news articles in `news_data` (in `.txt` or other supported formats).
   - Place financial reports (if available) in `reports_data`.

2. **Run the Orchestrator:**
   ```bash
   python orchestrator.py
   ```
   - This will initiate the multi-agent system. It will first prompt you for user input (or use the placeholder data). Then, it will fetch stock data, analyze news and reports, generate an investment strategy, provide advice, and explain the strategy.

### Troubleshooting

- **API Errors:** Make sure your Azure and OpenAI API keys and endpoints are correct.
- **Data Issues:** Verify that the `news_data` and `reports_data` folders contain valid data files.
- **Dependency Issues:** Ensure all required libraries are installed in your virtual environment. Refer to `requirements.txt`.
- **MLflow Errors:** If you are using MLflow, make sure the tracking server is running or the local database is correctly configured.
- **Other Errors:** If you encounter other issues, please refer to the project's documentation or open an issue on the GitHub repository.



## Future Enhancements

This project serves as a foundation for a comprehensive financial advisory system. There are numerous exciting directions for further development and enhancement:

### Core System Improvements

- **Real-time Data Integration:**
   - Integrate with real-time market data feeds (e.g., Alpaca, Interactive Brokers API) to provide up-to-the-minute analysis and decision-making.
   - Incorporate real-time news sentiment analysis from social media and financial news sources.
- **Advanced Machine Learning Models:**
   - Explore and implement more sophisticated machine learning models for stock price prediction, risk assessment, and portfolio optimization (e.g., time series forecasting, reinforcement learning).
   - Develop models to predict market trends based on macroeconomic indicators and alternative data sources.
- **Backtesting and Performance Evaluation:**
   - Implement a robust backtesting framework to evaluate the historical performance of generated investment strategies under different market conditions.
   - Track and analyze the performance of real trades executed by the system (once trading is fully implemented).

### User Experience and Interface

- **Interactive Web Application:**
   - Develop a user-friendly web interface (e.g., using React, Angular, or Vue.js) to provide a seamless user experience.
   - Allow users to input their financial information, preferences, and goals interactively.
   - Visualize portfolio performance, risk metrics, and investment recommendations.
- **Natural Language Interface:**
   - Enhance the User Interface Agent to understand complex financial queries posed in natural language.
   - Enable users to ask questions and receive personalized financial advice in a conversational manner.
- **Customizable Dashboards:**
   - Offer customizable dashboards to visualize relevant financial information based on user preferences.

### Expanded Functionality

- **Expanded Asset Classes:**
   - Support additional asset classes beyond stocks, such as bonds, commodities, cryptocurrencies, and real estate.
   - Develop specialized agents for each asset class to handle their unique characteristics.
- **Tax Optimization:**
   - Incorporate tax-aware investment strategies and advice.
   - Provide guidance on tax-loss harvesting and other tax optimization techniques.
- **Retirement Planning:**
   - Offer dedicated tools and advice for retirement planning, including simulations of different scenarios.
- **Educational Resources:**
   - Provide educational resources (articles, tutorials, videos) to help users understand financial concepts and make informed decisions.

### Advanced Features

- **Behavioral Finance Integration:**
   - Account for behavioral biases in decision-making (e.g., loss aversion, herding behavior) and provide personalized guidance to mitigate them.
- **Portfolio Rebalancing:**
   - Automatically rebalance portfolios to maintain desired asset allocations over time.
- **Stress Testing:**
   - Conduct stress tests on portfolios to assess their resilience to adverse market events.
- **Explainable AI (XAI):**
   - Enhance the explainability agent to provide more detailed and transparent explanations of the reasoning behind investment decisions, using techniques like LIME or SHAP.
- **Ethical and Responsible AI:**
   - Implement safeguards to prevent discriminatory or biased outcomes in financial advice.
   - Ensure transparency and accountability in the system's decision-making processes by documenting the data and logic used.

### Scalability and Performance

- **Distributed Architecture:**
   - Design a scalable architecture (e.g., using microservices or serverless functions) to handle a large number of users and data sources efficiently.
- **Optimized Data Processing:**
   - Explore and implement techniques to optimize data processing and reduce computational costs.
- **Parallel Computing:**
   - Leverage parallel computing (e.g., using libraries like Dask or Ray) to speed up computationally intensive tasks like model training and backtesting.

### Additional Enhancements

- **Financial Education and Gamification:**
   - Introduce interactive educational modules and gamification elements to help users learn about financial concepts and investing in a fun and engaging way.
- **Collaboration and Social Features:**
   - Allow users to share investment ideas, strategies, and performance with each other.
   - Create a community of users who can learn and collaborate together.
- **Integration with Financial Tools:**
   - Integrate with popular financial tools and platforms (e.g., Robinhood, M1 Finance) to enable seamless portfolio management and trading.
- **Multi-Lingual Support:**
   - Expand the system to support multiple languages to cater to a wider audience.
- **Personalization and Customization:**
   - Offer more granular personalization options for investment strategies and advice.
   - Allow users to customize their dashboards and data visualization preferences.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## Disclaimer

This project is a prototype and should not be used for actual financial decision-making. It is intended for educational and demonstration purposes only. Always consult with a qualified financial advisor before making any investment decisions.
```
