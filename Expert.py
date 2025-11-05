# Simple Expert System: Financial Investment Advisor

def investment_advisor(risk_level, amount, duration):
    if risk_level == "low":
        if duration < 3:
            return "Recommended Investment: Fixed Deposit or Savings Account"
        else:
            return "Recommended Investment: Government Bonds or Mutual Funds"
    
    elif risk_level == "medium":
        if amount < 50000:
            return "Recommended Investment: Balanced Mutual Funds"
        else:
            return "Recommended Investment: Index Funds or Blue Chip Stocks"
    
    elif risk_level == "high":
        if duration >= 3:
            return "Recommended Investment: Equity Shares or Cryptocurrency"
        else:
            return "Recommended Investment: Short-term Trading or ETFs"
    
    else:
        return "Invalid input. Please enter valid options."

# --- User Interface ---
print("=== Financial Investment Advisor Expert System ===")
risk_level = input("Enter your risk tolerance (low/medium/high): ").lower()
amount = float(input("Enter investment amount (in ₹): "))
duration = int(input("Enter investment duration (in years): "))

decision = investment_advisor(risk_level, amount, duration)
print("\nSystem Recommendation:", decision)
