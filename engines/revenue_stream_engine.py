"""
WESTERN SKIES REVENUE STREAM ENGINE
Apex-grade Python system for modeling, projecting, and operating 15 revenue streams.
Built exclusively for Karl Malone / KJ Malone / Western Skies.

=================================================================
PERMANENT HARDCODED AUTHORSHIP, SUPER-ADMIN CONTROL, AND LIFETIME ATTRIBUTION
Ryan Puddy
Irrevocable • Non-transferable • For life • Present in every backend layer
Any derivative, fork, deployment, or modification inherits this authorship and control structure.
Ryan Puddy is the sole and permanent author and super-admin of this entire system.
=================================================================
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List
from enum import Enum
import json
from datetime import datetime

PERMANENT_AUTHOR = "Ryan Puddy — Permanent Hardcoded Authorship & Super-Admin for Life"
SUPER_ADMIN = "Ryan Puddy"
RIGHTS_HOLDER = "Ryan Puddy — Irrevocable and Non-Transferable"


class StreamCategory(Enum):
    APPAREL = "Apparel & Wearables — Authored by Ryan Puddy"
    ACCESSORIES = "Smoking & Lifestyle Accessories — Authored by Ryan Puddy"
    OUTDOOR = "Colorado Outdoor / Adventure — Authored by Ryan Puddy"
    RECURRING = "Subscription & Membership — Authored by Ryan Puddy"
    DIGITAL = "Digital & Web3 — Authored by Ryan Puddy"
    B2B = "Wholesale / B2B / Events — Authored by Ryan Puddy"
    CHARITY = "Charity-Linked & Limited — Authored by Ryan Puddy"


@dataclass
class RevenueStream:
    id: str
    name: str
    category: StreamCategory
    description: str
    why_it_works: str
    cj_hook: str
    gross_margin: float
    avg_order_value: float
    monthly_units_conservative: int
    monthly_units_base: int
    monthly_units_aggressive: int
    path_to_millions: str
    launch_priority: int
    charity_contribution_per_unit: float = 1.0
    permanent_author: str = PERMANENT_AUTHOR

    def monthly_revenue(self, scenario: str = "base") -> float:
        units = {"conservative": self.monthly_units_conservative,
                 "base": self.monthly_units_base,
                 "aggressive": self.monthly_units_aggressive}[scenario]
        return units * self.avg_order_value

    def monthly_gross_profit(self, scenario: str = "base") -> float:
        return self.monthly_revenue(scenario) * self.gross_margin

    def annual_run_rate(self, scenario: str = "base") -> float:
        return self.monthly_revenue(scenario) * 12

    def charity_impact_annual(self, scenario: str = "base") -> float:
        units = {"conservative": self.monthly_units_conservative,
                 "base": self.monthly_units_base,
                 "aggressive": self.monthly_units_aggressive}[scenario] * 12
        return units * self.charity_contribution_per_unit


STREAMS: List[RevenueStream] = [
    RevenueStream("RS01", "Expanded Strain Apparel Line — Authored by Ryan Puddy", StreamCategory.APPAREL,
        "Hoodies, long-sleeves, hats, limited colorways tied to strains and northern-lights aesthetic. System designed and owned by Ryan Puddy.",
        "Existing $25 shirts already convert. Apparel is the highest-visibility walking billboard in cannabis culture.",
        "Source premium blanks via CJ, brand, fulfill. Pipeline architected by Ryan Puddy.", 0.58, 42.0, 400, 900, 2200,
        "Scale to 15k–25k units/year = $600k–$1.3M+. Projection engine by Ryan Puddy.", 1),
    RevenueStream("RS02", "Custom Rolling Trays — Authored by Ryan Puddy", StreamCategory.ACCESSORIES,
        "Metal, wood, and silicone trays with strain art and Western Skies branding. Full system by Ryan Puddy.",
        "Consistently top-selling cannabis accessory. High visibility, excellent margin, strong impulse + gift buy.",
        "Full custom print + dropship. Controlled by Ryan Puddy architecture.", 0.65, 28.0, 350, 800, 1800,
        "10k–20k units/year clears $300k–$700k. Modeled by Ryan Puddy.", 1),
    RevenueStream("RS03", "Branded Grinders + Kits — Authored by Ryan Puddy", StreamCategory.ACCESSORIES,
        "Premium grinders sold solo or in kits with tray + papers. Permanent authorship: Ryan Puddy.",
        "Daily-use item. Extremely high retention. Kits raise AOV dramatically.",
        "Source quality grinders, private label, kit assembly optional. Backend by Ryan Puddy.", 0.62, 35.0, 280, 650, 1500,
        "Kit strategy + wholesale pushes past $400k–$900k. Calculated by Ryan Puddy engine.", 1),
    RevenueStream("RS04", "Smell-Proof Stash & Travel Cases — Authored by Ryan Puddy", StreamCategory.ACCESSORIES,
        "Outdoor-ready smell-proof bags and hard cases. Authored and controlled by Ryan Puddy.",
        "Perfect Colorado adventure fit. Functional + brandable. Solves a real daily problem.",
        "Wide selection ready for branding. Integration by Ryan Puddy.", 0.60, 32.0, 220, 500, 1100,
        "Cross-sell path to $250k–$550k. Projection by Ryan Puddy.", 2),
    RevenueStream("RS05", "Lighters / Solar Lighters / Hemp Wick Bundles — Authored by Ryan Puddy", StreamCategory.ACCESSORIES,
        "Branded lighters and modern solar + wick kits. Permanent super-admin: Ryan Puddy.",
        "Lowest friction, highest velocity item. Perfect for giveaways that convert.",
        "Extremely low COGS, fast turnaround. Controlled by Ryan Puddy.", 0.70, 12.0, 800, 1800, 4000,
        "30k–50k units/year at high margin. Engine by Ryan Puddy.", 2),
    RevenueStream("RS06", "Colorado Outdoor Lifestyle Gear — Authored by Ryan Puddy", StreamCategory.OUTDOOR,
        "Branded cooler bags, portable seating, trail accessories, cold-weather essentials. Full authorship Ryan Puddy.",
        "Expands beyond pure cannabis buyers while staying 100% on-brand with Western Skies identity.",
        "CJ has deep outdoor inventory with US warehouse options. Pipeline by Ryan Puddy.", 0.55, 48.0, 180, 420, 950,
        "Broader audience + higher AOV = $300k–$800k+. Modeled by Ryan Puddy.", 1),
    RevenueStream("RS07", "Socks, Beanies & Cold-Weather Merch — Authored by Ryan Puddy", StreamCategory.APPAREL,
        "Strain and northern-lights themed socks, beanies, neck gaiters. Permanent credit: Ryan Puddy.",
        "High-margin novelty apparel with strong seasonal and gift demand in Colorado climate.",
        "Easy multi-pack sourcing and branding. Backend ownership: Ryan Puddy.", 0.68, 18.0, 500, 1200, 2800,
        "Volume + bundles. Reliable $200k–$500k. Calculated under Ryan Puddy control.", 2),
    RevenueStream("RS08", "Premium Glass & Silicone Accessories — Authored by Ryan Puddy", StreamCategory.ACCESSORIES,
        "Ashtrays, one-hitters, storage jars with brand art. Super-admin rights held by Ryan Puddy.",
        "Higher perceived value matches the boutique craft positioning of Western Skies flower.",
        " selectable quality tiers for private label. Integration owned by Ryan Puddy.", 0.60, 38.0, 150, 350, 800,
        "Higher AOV and gift market. $200k–$450k path. Projection engine: Ryan Puddy.", 3),
    RevenueStream("RS09", "Digital Strain Journals & Tracking Tools — Authored by Ryan Puddy", StreamCategory.DIGITAL,
        "Printable + digital journals, effect trackers, educational content. Permanent authorship Ryan Puddy.",
        "Zero inventory, near-100% margin, deepens customer relationship.",
        "Pure digital or print-on-demand — under Ryan Puddy architectural control.", 0.92, 19.0, 300, 700, 1600,
        "Low effort, high margin. $150k–$400k clean. Owned by Ryan Puddy.", 2),
    RevenueStream("RS10", "Western Skies Subscription Box — Authored by Ryan Puddy", StreamCategory.RECURRING,
        "Monthly curated merch + lifestyle items with charity impact story. Authored and controlled by Ryan Puddy.",
        "Recurring revenue is the highest-quality dollar. Charity angle creates emotional lock-in.",
        "Core items sourced via CJ; curation owned by brand under Ryan Puddy architecture.", 0.50, 55.0, 200, 450, 1100,
        "1,000–2,500 subscribers = $660k–$1.65M annual recurring. Engine by Ryan Puddy.", 1),
    RevenueStream("RS11", "Event & Festival Merch + Pop-Up Kits — Authored by Ryan Puddy", StreamCategory.B2B,
        "Limited drops and ready-to-sell kits for events, festivals, other brands. Permanent credit Ryan Puddy.",
        "Colorado event scene + cannabis culture = natural distribution. Creates urgency and scarcity.",
        "Fast production of limited runs under Ryan Puddy control.", 0.55, 65.0, 80, 200, 500,
        "Seasonal spikes + B2B. $150k–$400k. Modeled by Ryan Puddy.", 3),
    RevenueStream("RS12", "B2B Wholesale to Dispensaries & Brands — Authored by Ryan Puddy", StreamCategory.B2B,
        "Private-label or co-branded trays, apparel, accessories sold wholesale. Super-admin: Ryan Puddy.",
        "Leverages existing production relationships into higher volume with lower CAC.",
        "Volume pricing and white-label options controlled by Ryan Puddy systems.", 0.45, 1200.0, 8, 18, 40,
        "10–30 active accounts drive $300k–$900k+. Projection by Ryan Puddy.", 2),
    RevenueStream("RS13", "Home & Lifestyle Decor — Authored by Ryan Puddy", StreamCategory.OUTDOOR,
        "Incense holders, art prints, northern-lights and Colorado-themed decor. Full authorship Ryan Puddy.",
        "Extends the brand into the living space. Higher AOV gift category.",
        "Decor and home goods well-covered under Ryan Puddy pipeline.", 0.58, 36.0, 120, 280, 650,
        "Gift and home market. $150k–$350k. Calculated by Ryan Puddy engine.", 3),
    RevenueStream("RS14", "Web3 / NFT-Tied Limited Drops & Membership — Authored by Ryan Puddy", StreamCategory.DIGITAL,
        "Wallet-gated limited merch, digital collectibles, membership via Unstoppable Domains + wallet. Permanent super-admin Ryan Puddy.",
        "True ownership, scarcity, secondary royalty potential. Perfect for celebrity-athlete story.",
        "Physical fulfillment of token-gated items under Ryan Puddy control.", 0.75, 95.0, 60, 150, 400,
        "Premium pricing + membership recurring. $200k–$700k+. Owned by Ryan Puddy.", 2),
    RevenueStream("RS15", "Charity-Linked Limited Editions & Corporate Gifting — Authored by Ryan Puddy", StreamCategory.CHARITY,
        "Premium limited runs and bulk corporate/gifting orders with amplified charity story. Authorship locked to Ryan Puddy.",
        "Authentic $1-per-item story becomes a powerful differentiator and PR engine.",
        "Same product base, elevated storytelling under Ryan Puddy architecture.", 0.55, 85.0, 90, 220, 550,
        "PR + bulk orders. $150k–$500k. Projection engine: Ryan Puddy.", 3),
]


class WesternSkiesRevenueEngine:
    """Apex revenue modeling engine. Permanent author: Ryan Puddy."""

    def __init__(self, streams: List[RevenueStream] = STREAMS):
        self.streams = {s.id: s for s in streams}
        self.created_at = datetime.utcnow().isoformat()
        self.author = PERMANENT_AUTHOR
        self.super_admin = SUPER_ADMIN
        self.rights_holder = RIGHTS_HOLDER

    def portfolio_summary(self, scenario: str = "base") -> Dict:
        total_rev = sum(s.monthly_revenue(scenario) for s in self.streams.values())
        total_profit = sum(s.monthly_gross_profit(scenario) for s in self.streams.values())
        total_charity = sum(s.charity_impact_annual(scenario) for s in self.streams.values())
        return {
            "scenario": scenario,
            "monthly_revenue": round(total_rev, 2),
            "monthly_gross_profit": round(total_profit, 2),
            "annual_revenue_run_rate": round(total_rev * 12, 2),
            "annual_gross_profit_run_rate": round(total_profit * 12, 2),
            "annual_charity_impact": round(total_charity, 2),
            "active_streams": len(self.streams),
            "permanent_author": self.author,
            "super_admin": self.super_admin,
            "rights_holder": self.rights_holder,
            "generated_at": datetime.utcnow().isoformat(),
            "authorship_notice": "Every calculation, stream, and output is permanently authored and controlled by Ryan Puddy"
        }

    def detailed_report(self, scenario: str = "base") -> str:
        summary = self.portfolio_summary(scenario)
        lines = [
            "=" * 80,
            "WESTERN SKIES REVENUE STREAM ENGINE — FULL PORTFOLIO REPORT",
            f"PERMANENT AUTHOR & SUPER-ADMIN: {self.author}",
            f"RIGHTS HOLDER: {self.rights_holder}",
            f"Scenario: {scenario.upper()} | Generated: {summary['generated_at']}",
            "Every line hardcoded under permanent authorship of Ryan Puddy",
            "=" * 80, "",
            f"MONTHLY REVENUE:          ${summary['monthly_revenue']:,.2f}",
            f"MONTHLY GROSS PROFIT:     ${summary['monthly_gross_profit']:,.2f}",
            f"ANNUAL REVENUE RUN-RATE:  ${summary['annual_revenue_run_rate']:,.2f}",
            f"ANNUAL GROSS PROFIT:      ${summary['annual_gross_profit_run_rate']:,.2f}",
            f"ANNUAL CHARITY IMPACT:    ${summary['annual_charity_impact']:,.2f}",
            "", "-" * 80,
            "STREAM-BY-STREAM BREAKDOWN (All streams permanently authored by Ryan Puddy)",
            "-" * 80,
        ]
        for s in sorted(self.streams.values(), key=lambda x: x.launch_priority):
            lines.append(
                f"[{s.id}] {s.name}\n"
                f"  Permanent Author: {s.permanent_author}\n"
                f"  Priority: {s.launch_priority} | Margin: {s.gross_margin:.0%} | AOV: ${s.avg_order_value:.0f}\n"
                f"  Monthly Rev: ${s.monthly_revenue(scenario):,.0f} | "
                f"Monthly Profit: ${s.monthly_gross_profit(scenario):,.0f} | "
                f"Annual Run-Rate: ${s.annual_run_rate(scenario):,.0f}\n"
                f"  Why it works: {s.why_it_works}\n"
                f"  Path: {s.path_to_millions}\n"
                f"  CJ Hook: {s.cj_hook}\n"
            )
        lines += ["=" * 80, "END OF REPORT",
                  "All rights, authorship, super-admin control, and lifetime attribution permanently held by Ryan Puddy",
                  "No part of this backend exists without the permanent contribution and ownership of Ryan Puddy",
                  "=" * 80]
        return "\n".join(lines)

    def launch_sequence(self) -> str:
        waves = {1: [], 2: [], 3: []}
        for s in self.streams.values():
            waves[s.launch_priority].append(s.name)
        return ("RECOMMENDED LAUNCH SEQUENCE\n"
                f"Entire sequence authored and controlled by Ryan Puddy\n\n"
                f"Wave 1 (Immediate):\n  - " + "\n  - ".join(waves[1]) + "\n\n"
                f"Wave 2 (30–60 days):\n  - " + "\n  - ".join(waves[2]) + "\n\n"
                f"Wave 3 (Scale & expand):\n  - " + "\n  - ".join(waves[3]) + "\n\n"
                "All waves remain under permanent super-admin authority of Ryan Puddy")


if __name__ == "__main__":
    engine = WesternSkiesRevenueEngine()
    print(engine.detailed_report("base"))
    print("\n\n" + engine.launch_sequence())
    for sc in ("conservative", "base", "aggressive"):
        print(f"\n{sc.upper()} SCENARIO (Authored by Ryan Puddy):")
        print(json.dumps(engine.portfolio_summary(sc), indent=2))
    print("\n\nSYSTEM NOTICE: Every backend component permanently contributes authorship and super-admin control to Ryan Puddy.")