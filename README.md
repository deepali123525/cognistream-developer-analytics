# CogniStream – Developer Flow-State & Cognitive Load Analytics

## Project Overview
CogniStream is a Python-based data analytics project that explores developer productivity, coding activity, focus time, interruptions, and flow-state patterns using simulated developer activity data.

## Objectives
- Analyze developer coding activity.
- Measure coding time and focus hours.
- Identify interruptions.
- Calculate potential flow-state sessions.
- Visualize developer productivity metrics.

## Technologies Used
- Python
- Pandas
- Polars
- Streamlit
- Plotly
- CSV

## Project Features
- Simulated developer activity dataset
- Developer productivity analysis
- Focus hours and coding time calculations
- Interruption analysis
- Flow-state metrics
- Interactive Streamlit dashboard

## Project Structure
```text
CogniStream/
├── generate_data.py
├── analyze_flow.py
├── flow_metrics.py
├── dashboard.py
├── developer_activity.csv
├── developer_summary.csv
├── flow_metrics.csv
└── README.md
```

## How to Run

Install dependencies:

```bash
pip install pandas polars streamlit plotly
```

Generate data:

```bash
python generate_data.py
```

Run analysis:

```bash
python analyze_flow.py
python flow_metrics.py
```

Launch dashboard:

```bash
streamlit run dashboard.py
```

## Project Status
This project is a work in progress. Python-based data generation, analytics, flow metrics, and the Streamlit dashboard have been developed. Further integration of Apache Airflow, ClickHouse, and FastAPI is planned.

## Learning Outcomes
- Data generation and preprocessing
- Data analysis using Pandas and Polars
- Developer productivity metrics
- Interactive dashboard development
- Data visualization using Plotly
  
