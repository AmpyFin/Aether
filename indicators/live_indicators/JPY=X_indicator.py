"""
USD/JPY (JPY=X) Indicator

Role: Classic risk barometer via yen funding and rate differentials
Transform: Log price; tightly paired with ^TNX

Key Parameters:
- Horizon focus: 1d and 1w measurements
- Primary metrics: z_v_1d, z_v_5d
- Paired indicators: ^TNX z_v_1d, HYG, UUP

Signals & Triggers:
1. Rates-led Risk-off:
   - ^TNX z_v_1d ≥ +0.8 and
   - USDJPY z_v_1d ≥ +0.6 (USD↑/JPY↓)
   - Often impacts cyclical sectors

2. Growth-scare Risk-off:
   - ^TNX z_v_1d ≤ -0.8 and
   - USDJPY z_v_1d ≤ -0.6 (JPY safe-haven bid)

3. Re-risking:
   - USDJPY z_v_5d ≥ +0.5
   - With HYG improving
   - UUP flat/down

Known Quirks:
- BoJ policy headline sensitivity
- MoF interventions can cause sudden reversals
"""
