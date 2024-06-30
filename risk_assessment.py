import pandas as pd
from llama_index.core.tools import FunctionTool
import numpy as np

def assess_risk(historical_data):
    df = pd.DataFrame(historical_data)
    volatility = df['Close'].pct_change().std() * np.sqrt(252)  # Annualized volatility
    return {"volatility": volatility}

risk_assessment_tool = FunctionTool.from_defaults(assess_risk, name="RiskAssessmentTool", description="Assess risk of an investment based on historical data")

