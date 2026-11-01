# Personal Agent Total Daily Energy Expenditure Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency precision TDEE modeler, Cunningham lean body mass BMR calculator, macronutrient TEF partitioner, and adaptive thermogenesis plateau detector.

## Architecture

```mermaid
flowchart TD
    Biometrics[LBM, Total Mass, Steps, Macros] --> TDEEKernel[Multi-Compartment TDEE Engine]
    TDEEKernel --> BMR[Cunningham BMR: 500 + 22*LBM]
    TDEEKernel --> NEAT[NEAT Ambulation Thermogenesis]
    TDEEKernel --> TEF[Macronutrient Specific TEF]
    TDEEKernel --> TDEESum[Total Maintenance Caloric Flux]
    TimeSeries[Multi-Week Scale Weight & Daily Intake] --> AdaptDetector[Adaptive Thermogenesis Detector]
    AdaptDetector --> RefeedPrescription[Structured Refeed / Diet Break Protocol]
```

## Quickstart

```python
from client import PersonalAgentTotalDailyEnergyExpenditure

agent = PersonalAgentTotalDailyEnergyExpenditure()
res = agent.calculate_precision_tdee(lean_mass_kg=62.0, total_mass_kg=75.0, daily_steps=10000)
print(f"Maintenance TDEE: {res['calculated_tdee_maintenance_kcal']} kcal/day")
```
