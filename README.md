# 🚒 London Fire Brigade — Operational & Geospatial Analysis

End-to-end data analysis project based on public London Fire Brigade data, focused on operational performance (response times) and spatial patterns to support decision-making.

## 🎯 Objectives
- Measure response-time performance across areas
- Produce operational KPIs and identify slow-response zones
- Prepare clean datasets for dashboarding in Power BI

## 📁 Dataset
Public London Fire Brigade incident data (not included in this repository).

**Note:** raw data is not shared due to size/licensing constraints. This repository contains the full pipeline and outputs structure.

## 🔄 Project pipeline
1. Load raw data (`src/load_data.py`)
2. Clean & build response time metric (`src/clean_data.py`)
3. Compute KPI tables for Power BI (`src/analysis_kpis.py`)
4. Build the dashboard in Power BI (`powerbi/`)

## ▶️ Run the project
```bash
pip install -r requirements.txt
python src/load_data.py
python src/clean_data.py
python src/analysis_kpis.py
