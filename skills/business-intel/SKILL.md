---
name: business-intel
description: "Analyze market trends, financial growth (CAGR), and business intelligence data. Use when: (1) Researching market demand or 'Google Trends' for business ideas, (2) Calculating Compound Annual Growth Rate (CAGR) for business planning, (3) Auditing market signals to validate business feasibility."
---

# Business Intelligence (Market Analysis & Growth)

Use this skill to validate business signals and calculate growth trajectories during the "Idea Validation" and "Scaling" phases of the Launch Sequence.

## Google Trends & Market Demand
When researching a business niche, identify the "search volume signal" to see if demand is growing or shrinking.

### Procedure
1. Use `scripts/google_trends.py` to simulate or fetch trend data for a specific niche.
2. Cross-reference with `web_search` for qualitative sentiment (Hacker News, Reddit, Industry reports).

```bash
python3 skills/business-intel/scripts/google_trends.py "agentic ai automation"
```

## Financial Growth (CAGR)
Compound Annual Growth Rate (CAGR) provides a smoothed annual rate of growth over a specific time period. Use this to project future scale or audit historical performance.

### Formula
`CAGR = [(Ending Value / Beginning Value) ^ (1 / Number of Years)] - 1`

### Procedure
Use `scripts/cagr_calc.py` to calculate the growth percentage.

```bash
# Calculate CAGR for growth from $10k to $100k over 3 years
python3 skills/business-intel/scripts/cagr_calc.py 10000 100000 3
```

## Launch Sequence Integration
- **Stage 2 (Validation):** Use CAGR to verify if a niche has the historical growth required for a sustainable exit.
- **Stage 4 (Scaling):** Use Trend data to identify when to pivot or double down on specific marketing channels.
