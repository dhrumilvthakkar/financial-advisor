import cvxpy as cp
import numpy as np
from llama_index.core.tools import FunctionTool

def optimize_portfolio(expected_returns, covariances, risk_tolerance):
    """Optimizes portfolio allocation based on inputs.

    Args:
        expected_returns (np.array): Array of expected returns for each asset.
        covariances (np.array): Covariance matrix of asset returns.
        risk_tolerance (float): Investor's risk tolerance (higher value means more risk aversion).

    Returns:
        np.array: Optimal weights for each asset in the portfolio.
    """
    n = len(expected_returns)
    w = cp.Variable(n)
    ret = expected_returns.T @ w
    risk = cp.quad_form(w, covariances)
    target_return = cp.Parameter(nonneg=True)
    constraints = [cp.sum(w) == 1, w >= 0, ret >= target_return]
    prob = cp.Problem(cp.Maximize(ret - risk_tolerance * risk), constraints)

    target_return.value = 0  # Start with minimum return
    prob.solve()

    return w.value

portfolio_optimization_tool = FunctionTool.from_defaults(
    optimize_portfolio,
    name="PortfolioOptimizationTool",
    description="Optimize portfolio allocation based on expected returns, covariances, and risk tolerance."
)
