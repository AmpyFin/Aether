"""
High-Yield Credit (HYG) Indicator

Role: Fast proxy for credit spreads and risk appetite
Transform: Log price and HYG/LQD log-ratio tracking

Key Parameters:
- Horizon focus: 1d shock, 1w follow-through
- Primary metrics: z_v_1d (1-day velocity z-score), z_v_5d (5-day velocity z-score)
- Secondary: z_a_1d (1-day acceleration z-score)

Signals & Triggers:
1. De-risking:
   - z_v_1d ≤ -1.0 or z_v_5d ≤ -0.8
   - Signal strengthens if UUP rising and VIX rising

2. Capitulation:
   - z_a_1d ≤ -0.8 when z_v_5d is already negative

3. Market Healing:
   - z_v_5d ≥ +0.5 and HYG/LQD z_v_5d ≥ +0.5

Known Quirks:
- Ex-dividend date drops can affect readings
- Mild rate sensitivity
- Morning liquidity thinner than SPY
"""
