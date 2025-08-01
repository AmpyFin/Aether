"""
Credit Stress Proxy (HYG/LQD) Indicator

Role: High signal-to-noise ratio derived indicator for credit stress
Transform: Log-ratio of HYG to LQD

Key Parameters:
- Horizon focus: 5d for trend confirmation
- Primary metric: z_v_5d (5-day velocity z-score)

Signals & Triggers:
1. Risk-off Credit Widening:
   - z_v_5d ≤ -0.8 (widening-like move)
   - Confirms credit market stress

2. Credit Market Healing:
   - z_v_5d ≥ +0.5
   - Indicates improving credit conditions

Benefits:
- Cleaner signal than individual components
- Filters out rate-only moves
- Good confirmation for other risk indicators
"""
