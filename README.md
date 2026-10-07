# 📊 Regional Retail Catchment & Profitability Dashboard

![Dashboard Preview](dashboard_preview.png) <img width="1855" height="847" alt="image" src="https://github.com/user-attachments/assets/bee9798c-70e1-4f5b-94af-e70a2684230f" />


## 📌 Business Objective
This project transforms a raw, mathematically complex dataset of 5,000+ supermarket transactions into an interactive executive dashboard. The goal is to track regional sales performance, map spatial market catchments, and automate complex partner profit-sharing calculations.

## 🛠️ Technology Stack
* **Python:** Core data processing and algorithm logic.
* **Pandas:** Data cleaning, missing value imputation, and spatial aggregation.
* **Plotly:** Interactive geographic and time-series data visualization.
* **Streamlit:** Rapid deployment of the analytical web application.

## 💡 Key Business Insights Discovered
1. **The Profit Illusion:** While overall revenue numbers were high, the automated profit-sharing algorithm revealed true net margins are heavily impacted by partner tier structures.
2. **Category Performance:** The "Snacks" category proved to be the highest driver of true net profit, outperforming higher-priced staple items.
3. **Spatial Catchment:** The East region emerged as the most profitable geographic zone, indicating a need to scale inventory distribution to those coordinates.

## 🚀 How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python -m streamlit run dashboard_p1.py`
