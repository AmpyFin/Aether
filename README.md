# Aether-Model

A sophisticated market analysis system that identifies macrotrends using a combination of technical indicators and market sentiment analysis. The system focuses on what has already happened rather than predictions, providing clear signals through various market conditions.

## Core Indicators

### Live Indicators

1. **High-Yield Credit (HYG)**
   - Fast proxy for credit spreads/risk appetite
   - Key metrics: Log price, HYG/LQD ratio
   - Primary signals: De-risking, Capitulation, Healing

2. **Investment-Grade Credit (LQD)**
   - Quality + duration indicator
   - Helps distinguish rates shock vs growth scare
   - Paired with HYG and ^TNX

3. **US Dollar Proxy (UUP)**
   - Global de-risking/USD liquidity pulse
   - Intraday preferred over DX-Y.NYB
   - Risk-off surge and relief patterns

4. **US 10Y Yield Index (^TNX)**
   - Rates/inflation shock vs growth discriminator
   - Level changes and z-scores
   - Paired with LQD/GC for context

5. **Gold Futures (GC=F)**
   - Safety + real-rate thermometer
   - Headline reaction and macro shift patterns
   - Geopolitical stress indicator

6. **USD/JPY (JPY=X)**
   - Classic risk barometer
   - Yen funding and rate differential insights
   - Multiple risk-off patterns

### Derived Indicators

1. **Credit Stress Proxy (HYG/LQD)**
   - High signal-to-noise ratio
   - Cleaner credit stress readings
   - Widening and healing signals

2. **Growth vs Safety (GC=F/^TNX)**
   - Real-rate environment assessment
   - Simplified gold vs yields context
   - Trend confirmation tool

## Velocity Indicators (/velocity_indicator)

Each core indicator includes velocity measurements across multiple timeframes:

- 1-day (v_1d): Immediate momentum
- 1-week (v_5d): Short-term trend
- 1-month (v_20d): Medium-term direction

Velocity indicators are calculated as log-returns and normalized to z-scores for comparison across instruments.

## Acceleration Indicators (/acceleration_indicators)

Acceleration metrics capture rate-of-change in velocity, providing early warning signals:

- 1-day (a_1d): Shock detection
- 1-week (a_5d): Trend acceleration
- 1-month (a_20d): Sustained momentum shifts

Acceleration indicators are particularly useful for:
- Identifying capitulation events
- Spotting trend exhaustion
- Confirming momentum shifts

## Implementation Notes

- All indicators use log-transforms where appropriate
- Z-scores are calculated on rolling windows
- Velocity and acceleration metrics are computed for all core indicators
- Cross-confirmation between indicators enhances signal quality
- Known quirks (e.g., ex-dividend dates, contract rolls) are accounted for

## Market Indices Reference

- S&P 500
- Dow Jones Industrial Average
- Nasdaq Composite
- Russell 2000 Index
- NYSE Composite

This system is designed to identify current market conditions and regime shifts rather than predict future movements.