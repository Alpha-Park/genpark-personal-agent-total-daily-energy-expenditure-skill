---
name: genpark-personal-agent-total-daily-energy-expenditure-skill
version: "1.0.0"
description: "Zero-dependency precision TDEE modeler, Cunningham lean body mass BMR calculator, macronutrient TEF partitioner, and adaptive thermogenesis plateau detector."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Total Daily Energy Expenditure Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to manage physical energy balance, optimize body composition protocols, and detect metabolic adaptation plateaus during nutritional deficits.

## Agent In-Context Capabilities

- **Cunningham Lean Body Mass BMR**: Uses exact fat-free mass ($500 + 22 	imes LBM$) for accurate baseline estimation.
- **NEAT & TEF Partitioning**: Separates non-exercise activity thermogenesis and macronutrient-specific thermic costs (protein 25%, carbs 7.5%, fat 2.5%).
- **Adaptive Thermogenesis Detection**: Analyzes multi-week intake vs scale weight trends to quantify metabolic downshifts and prescribe refeed cycles.

## Tools Summary

1. `calculate_precision_tdee`: Computes exact maintenance calories and deficit/surplus boundaries.
2. `detect_metabolic_adaptation`: Identifies metabolic adaptation drops and recommends structured refeeds.
