# Marketplace Buy Box Suppression Repricer & Margin Guard Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Amazon reference price buy box suppression detector, off-Amazon competitive pricing floor sync, and algorithmic buy-box restoration re-pricer. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `diagnose_buy_box_suppression_cause`: Identify root cause of Buy Box suppression (External Competitive Price vs List Price Anchor violation).
- `synthesize_buy_box_restoration_price`: Compute optimal restoration price to regain Buy Box without breaching profitability floor.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_marketplace_buy_box_suppression_repricer_skill.server --test
```
