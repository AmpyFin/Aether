"""
Growth vs Safety (GC=F/^TNX) Indicator - Reactionary Derived

Role: Optional derived indicator for real-rate environment assessment
Transform: Log-ratio of Gold to 10Y Yield for cleaner real-rate signals

Key Parameters:
- Horizon focus: 5d for trend confirmation
- Primary metric: z_v_5d (5-day velocity z-score)
- Optional if already using GC=F and ^TNX separately
- Reactionary nature: Provides confirmation of primary indicator signals

Signals & Triggers:
1. Real-Rate Tailwind:
   - z_v_5d ≥ +0.7
   - Indicates favorable real-rate environment
   - Most reliable when aligned with individual GC=F and ^TNX moves

2. Real-Rate Headwind:
   - z_v_5d ≤ -0.7
   - Suggests challenging real-rate environment
   - Confirms stress signals from primary indicators

Benefits:
- Simplified real-rate proxy
- Helps confirm gold moves vs yield context
- Alternative to more complex real-rate calculations
- Reduces noise from individual instrument quirks

Usage Notes:
- Best used as confirmation of primary GC=F and ^TNX signals
- More reliable than single-instrument signals for regime shifts
- Particularly useful during periods of yield volatility
- Helps filter out false positives from individual instruments

Note: This is a supplementary indicator that provides cleaner reads
through ratio analysis while maintaining connection to core indicators
"""
