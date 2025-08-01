"""
Gold Futures Front Month (GC=F) Indicator

Role: Safety and real-rate thermometer
Transform: Log price; optional real-rate proxy with ^TNX (↓ real = gold ↑)

Key Parameters:
- Horizon focus: 1d spikes (headlines), 1w (macro shifts)
- Primary metrics: z_v_1d, z_a_1d
- Paired indicators: ^TNX z_v_1d, UUP z_v_1d

Signals & Triggers:
1. Safety/Real-Rate Bid:
   - z_v_1d ≥ +0.8 AND
   - ^TNX z_v_1d ≤ -0.5
   - Stronger signal if UUP not rising

2. Geopolitical Stress:
   - GC=F z_v_1d ≥ +0.8
   - With UUP z_v_1d ≥ +0.5 (gold ↑ despite USD ↑)

3. Fade Risk:
   - z_a_1d ≤ -0.7 after large 1-2 day increase

Known Quirks:
- Contract roll impacts
- Asia session gaps
- CTA trend amplification
"""
