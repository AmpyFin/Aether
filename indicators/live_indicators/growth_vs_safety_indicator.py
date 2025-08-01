"""
Growth vs Safety (GC=F/^TNX) Indicator

Role: Optional derived indicator for real-rate environment assessment
Transform: Log-ratio of Gold to 10Y Yield

Key Parameters:
- Horizon focus: 5d for trend confirmation
- Primary metric: z_v_5d (5-day velocity z-score)
- Optional if already using GC=F and ^TNX separately

Signals & Triggers:
1. Real-Rate Tailwind:
   - z_v_5d ≥ +0.7
   - Indicates favorable real-rate environment

Benefits:
- Simplified real-rate proxy
- Helps confirm gold moves vs yield context
- Alternative to more complex real-rate calculations

Note: This is a supplementary indicator that can be used alongside 
individual GC=F and ^TNX indicators for confirmation
"""
