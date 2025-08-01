"""
Investment-Grade Credit (LQD) Indicator

Role: Quality + duration indicator that helps disambiguate rates shock vs growth scare
Transform: Log price, paired with HYG and ^TNX for analysis

Key Parameters:
- Horizon focus: 1d and 1w measurements
- Primary metrics: z_v_1d, z_v_5d
- Paired indicators: HYG z_v_5d, ^TNX z_v_5d

Signals & Triggers:
1. Growth Scare Pattern:
   - LQD z_v_5d ≥ +0.5
   - While HYG z_v_5d ≤ -0.5
   - And ^TNX z_v_5d ≤ -0.5

2. Rates Shock Pattern:
   - LQD z_v_1d ≤ -0.8
   - With ^TNX z_v_1d ≥ +0.8

Known Quirks:
- Long duration makes it sensitive to yield movements
- Ex-dividend effects can impact readings
"""
