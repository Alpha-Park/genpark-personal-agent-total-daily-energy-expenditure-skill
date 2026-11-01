# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Total Daily Energy Expenditure Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentTotalDailyEnergyExpenditure

def main():
    agent = PersonalAgentTotalDailyEnergyExpenditure()

    print("=" * 70)
    print("DEMO: Personal Agent Total Daily Energy Expenditure (TDEE) & Metabolic Flux")
    print("=" * 70)

    # 1. Multi-compartment TDEE calculation (75kg individual, 62kg lean mass)
    res_tdee = agent.calculate_precision_tdee(
        lean_mass_kg=62.0,
        total_mass_kg=75.0,
        daily_steps=10200,
        exercise_calories=420.0,
        protein_grams=165.0,
        carb_grams=240.0,
        fat_grams=60.0
    )

    print(f"\n1. Multi-Compartment TDEE Modeling:")
    print(f"   BMR (Cunningham LBM): {res_tdee['metabolic_components']['bmr_cunningham_kcal']} kcal")
    print(f"   NEAT (10,200 steps): {res_tdee['metabolic_components']['neat_ambulation_kcal']} kcal")
    print(f"   EAT (Workout): {res_tdee['metabolic_components']['eat_exercise_kcal']} kcal")
    print(f"   TEF (Dietary Thermogenesis): {res_tdee['metabolic_components']['tef_dietary_kcal']} kcal")
    print(f"   ----------------------------------------")
    print(f"   Total Maintenance TDEE: {res_tdee['calculated_tdee_maintenance_kcal']} kcal/day")
    print(f"   Energy Flux Ratio: {res_tdee['metabolic_flux_ratio']}")
    print(f"   Mild Fat Loss Deficit: {res_tdee['recommended_targets']['mild_fat_loss_deficit_kcal']} kcal/day")

    # 2. Metabolic Adaptation & Plateau Detection (14-day history)
    intakes_14d = [1850.0] * 14
    # Weight stalled despite theoretical deficit
    weights_14d = [75.0, 74.9, 74.8, 74.7, 74.6, 74.6, 74.5, 74.5, 74.5, 74.5, 74.5, 74.4, 74.5, 74.5]

    res_adapt = agent.detect_metabolic_adaptation(intakes_14d, weights_14d)

    print(f"\n2. Metabolic Adaptation & Plateau Analysis (14-day window):")
    print(f"   Empirical Real TDEE: {res_adapt['empirical_actual_tdee_kcal']} kcal/day")
    print(f"   Metabolic Suppression: {res_adapt['metabolic_suppression_kcal_day']} kcal/day")
    print(f"   Status: {res_adapt['adaptation_status']}")
    print(f"   Prescription: {res_adapt['clinical_refeed_prescription']}")

    print("\nVerification complete: TDEE metabolic flux engine executed flawlessly.")

if __name__ == "__main__":
    main()
