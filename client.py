# -*- coding: utf-8 -*-
"""
Personal Agent Total Daily Energy Expenditure Client
Zero-dependency precision TDEE modeler, Cunningham lean body mass BMR calculator,
macronutrient TEF partitioner, and adaptive thermogenesis plateau detector.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentTotalDailyEnergyExpenditure:
    """
    Models total daily human metabolic flux, separating basal metabolic rate (Cunningham LBM formula),
    NEAT spontaneous ambulation, exercise energy expenditure (EAT), and adaptive thermogenesis.
    """

    def calculate_precision_tdee(
        self,
        lean_mass_kg: float,
        total_mass_kg: float,
        daily_steps: int = 8500,
        exercise_calories: float = 350.0,
        protein_grams: float = 140.0,
        carb_grams: float = 220.0,
        fat_grams: float = 65.0
    ) -> Dict[str, Any]:
        """
        Calculates exact multi-compartment TDEE:
        BMR (Cunningham) = 500 + 22 * LBM(kg)
        NEAT = 0.04 kcal/step * (TotalMass / 70.0)
        TEF = 0.25 * ProteinKcal + 0.075 * CarbKcal + 0.025 * FatKcal
        TDEE = BMR + NEAT + EAT + TEF
        """
        lbm = max(25.0, min(140.0, float(lean_mass_kg)))
        mass = max(lbm, min(220.0, float(total_mass_kg)))
        steps = max(500, min(50000, int(daily_steps)))
        eat = max(0.0, min(3000.0, float(exercise_calories)))
        p_g = max(0.0, min(500.0, float(protein_grams)))
        c_g = max(0.0, min(800.0, float(carb_grams)))
        f_g = max(0.0, min(300.0, float(fat_grams)))

        # 1. Cunningham Basal Metabolic Rate
        bmr = round(500.0 + (22.0 * lbm), 1)

        # 2. Non-Exercise Activity Thermogenesis (NEAT) from step ambulation
        mass_scaling = mass / 70.0
        neat = round(steps * 0.04 * mass_scaling, 1)

        # 3. Thermic Effect of Food (TEF)
        p_kcal = p_g * 4.0
        c_kcal = c_g * 4.0
        f_kcal = f_g * 9.0
        total_diet_kcal = round(p_kcal + c_kcal + f_kcal, 1)

        tef_protein = p_kcal * 0.25
        tef_carb = c_kcal * 0.075
        tef_fat = f_kcal * 0.025
        tef_total = round(tef_protein + tef_carb + tef_fat, 1)

        # 4. Total Daily Energy Expenditure
        tdee = round(bmr + neat + eat + tef_total, 1)

        # Energy flux ratio (total turnover relative to BMR)
        flux_ratio = round(tdee / bmr, 2)

        return {
            "lean_body_mass_kg": lbm,
            "total_body_mass_kg": mass,
            "metabolic_components": {
                "bmr_cunningham_kcal": bmr,
                "neat_ambulation_kcal": neat,
                "eat_exercise_kcal": eat,
                "tef_dietary_kcal": tef_total
            },
            "dietary_caloric_intake": total_diet_kcal,
            "calculated_tdee_maintenance_kcal": tdee,
            "daily_caloric_balance_kcal": round(total_diet_kcal - tdee, 1),
            "metabolic_flux_ratio": f"{flux_ratio}x BMR",
            "recommended_targets": {
                "mild_fat_loss_deficit_kcal": round(tdee * 0.82),
                "aggressive_fat_loss_deficit_kcal": round(tdee * 0.72),
                "lean_hypertrophy_surplus_kcal": round(tdee * 1.08)
            }
        }

    def detect_metabolic_adaptation(
        self,
        caloric_intake_history: List[float],
        scale_weight_history_kg: List[float]
    ) -> Dict[str, Any]:
        """
        Detects adaptive thermogenesis (metabolic slowdown) by comparing theoretical
        weight loss (7700 kcal / kg) against observed empirical scale weight trends.
        """
        if not caloric_intake_history or not scale_weight_history_kg:
            return {"error": "Missing historical intake or weight data"}

        days = min(len(caloric_intake_history), len(scale_weight_history_kg))
        if days < 7:
            return {"error": "At least 7 consecutive daily data points required for metabolic adaptation detection."}

        intakes = [float(x) for x in caloric_intake_history[:days]]
        weights = [float(x) for x in scale_weight_history_kg[:days]]

        avg_daily_intake = sum(intakes) / days
        weight_delta_kg = weights[-1] - weights[0]

        # In standard metabolism, 1 kg body mass delta ~= 7700 kcal energy imbalance
        observed_daily_imbalance = (weight_delta_kg * 7700.0) / days
        estimated_real_tdee = avg_daily_intake - observed_daily_imbalance

        # Estimate expected initial TDEE from initial weight (approx 33 kcal / kg)
        theoretical_initial_tdee = weights[0] * 33.0
        adaptation_kcal_drop = round(theoretical_initial_tdee - estimated_real_tdee, 1)

        if adaptation_kcal_drop > 250.0:
            status = "SIGNIFICANT ADAPTIVE THERMOGENESIS DETECTED"
            action = "Implement a 7-14 day full diet break at maintenance calories to restore leptin, thyroid T3, and NEAT levels."
        elif adaptation_kcal_drop > 100.0:
            status = "MILD METABOLIC DOWNSHIFT"
            action = "Incorporate 48-hour refeed containing high complex carbohydrates (+400 kcal above deficit)."
        else:
            status = "OPTIMAL METABOLIC RATE (NO DETECTABLE ADAPTATION)"
            action = "Current caloric deficit is well-tolerated. Continue present pacing."

        return {
            "analysis_window_days": days,
            "average_daily_intake_kcal": round(avg_daily_intake, 1),
            "observed_weight_delta_kg": round(weight_delta_kg, 2),
            "empirical_actual_tdee_kcal": round(estimated_real_tdee, 1),
            "metabolic_suppression_kcal_day": adaptation_kcal_drop,
            "adaptation_status": status,
            "clinical_refeed_prescription": action
        }
