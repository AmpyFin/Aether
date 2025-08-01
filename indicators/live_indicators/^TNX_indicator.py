"""
US 10y Yield Index (^TNX) Indicator

Role: Discriminator between rates/inflation shock and growth scare
Transform: Level changes (bps) and log for z-scores; paired with LQD/GC

Key Parameters:
- Horizon focus: 1d for shocks, 1w for regime turns
- Primary metrics: Δ^TNX_1d (1-day change), z_v_5d
- Paired indicators: LQD, UUP, HYG, GC=F

Signals & Triggers:
1. Rates Shock:
   - Δ^TNX_1d ≥ +10-15 bps (index +1.0-1.5) or
   - z_v_5d ≥ +0.8
   - Expected correlations: LQD ↓, UUP ↑, HYG ↓

2. Growth Scare:
   - Δ^TNX_1d ≤ -10-15 bps
   - With correlations: LQD ↑, GC=F ↑, HYG ↓

Known Quirks:
- CPI/Fed announcement day volatility
- Treasury auction impacts
- Index scaling (42.5 ≈ 4.25%)
"""
