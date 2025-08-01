"""
US Dollar Proxy (UUP) Indicator

Role: Global de-risking and USD liquidity pulse indicator
Transform: Log price (alternative: DX index with same logic)

Key Parameters:
- Horizon focus: 1d and 1w measurements
- Primary metrics: z_v_5d, v_1d (1-day velocity)
- Paired indicators: HYG z_v_5d

Signals & Triggers:
1. Risk-off USD Surge:
   - z_v_5d ≥ +0.8 or
   - v_1d ≥ +0.5% with HYG z_v_5d ≤ -0.5

2. Market Relief:
   - z_v_5d ≤ -0.5
   - Concurrent with HYG improvement

Known Quirks:
- Month-end rebalancing can affect readings
- DXY basket is EUR-heavy - cross-check with JPY=X recommended
"""
