# -*- coding: utf-8 -*-
"""Buy Box Suppression Repricer Guard for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class BuyBoxSuppressionRepricerGuard:
    @staticmethod
    def diagnose_buy_box_suppression_cause(current_listing_price_usd: float, amazon_reference_price_usd: float, min_margin_floor_usd: float, walmart_lowest_price_usd: float = 0.0) -> Dict[str, Any]:
        external_trigger = (walmart_lowest_price_usd > 0 and walmart_lowest_price_usd < current_listing_price_usd)
        internal_anchor = (current_listing_price_usd > amazon_reference_price_usd)
        
        is_suppressed = external_trigger or internal_anchor
        target_reclaim_price = min(amazon_reference_price_usd, walmart_lowest_price_usd if walmart_lowest_price_usd > 0 else amazon_reference_price_usd)
        
        can_meet_price = target_reclaim_price >= min_margin_floor_usd
        
        return {
            "current_price": current_listing_price_usd,
            "is_buy_box_suppressed": is_suppressed,
            "trigger_reason": "OFF_AMAZON_EXTERNAL_PRICE_MATCH" if external_trigger else ("INTERNAL_ANCHOR_EXCEEDED" if internal_anchor else "NONE"),
            "target_restoration_price_usd": target_reclaim_price,
            "margin_floor_usd": min_margin_floor_usd,
            "safe_to_reprice": can_meet_price
        }

    @staticmethod
    def synthesize_buy_box_restoration_price(target_competitive_price_usd: float, min_margin_floor_usd: float) -> Dict[str, Any]:
        recommended_price = max(min_margin_floor_usd, round(target_competitive_price_usd - 0.01, 2))
        return {
            "recommended_repricing_point_usd": recommended_price,
            "margin_safety_spread_usd": round(recommended_price - min_margin_floor_usd, 2),
            "reprice_execution_command": f"SET_PRICE {recommended_price} USD VIA_SP_API"
        }
