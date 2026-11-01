# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Total Daily Energy Expenditure Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentTotalDailyEnergyExpenditure

mcp = FastMCP("PersonalAgentTotalDailyEnergyExpenditure")
client = PersonalAgentTotalDailyEnergyExpenditure()

@mcp.tool()
def calculate_precision_tdee(
    lean_mass_kg: float,
    total_mass_kg: float,
    daily_steps: int = 8500,
    exercise_calories: float = 350.0,
    protein_grams: float = 140.0,
    carb_grams: float = 220.0,
    fat_grams: float = 65.0
) -> str:
    """Calculates exact multi-compartment TDEE (BMR + NEAT + EAT + TEF) from body composition and macros."""
    import json
    return json.dumps(client.calculate_precision_tdee(
        lean_mass_kg, total_mass_kg, daily_steps, exercise_calories, protein_grams, carb_grams, fat_grams
    ), indent=2)

@mcp.tool()
def detect_metabolic_adaptation(
    caloric_intake_history: list[float],
    scale_weight_history_kg: list[float]
) -> str:
    """Detects adaptive thermogenesis and prescribes diet breaks/refeeds based on weight-intake regression."""
    import json
    return json.dumps(client.detect_metabolic_adaptation(
        caloric_intake_history, scale_weight_history_kg
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
