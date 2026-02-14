# 🚀 Real-Time AI Sales Pipeline & Anomaly Detector
**Architecting Sub-Second Latency Data Streams for Market Intelligence**

## 📌 Project Overview
This project simulates a high-frequency retail environment where sales data is ingested, processed, and analyzed in real-time. The system is designed to identify "price anomalies" (outliers with >50% deviation) using a heuristic-based detection engine, providing immediate business alerts.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Engine:** DuckDB (for high-speed analytical processing)
- **Libraries:** Pandas, NumPy, Faker (Data Simulation)
- **Logic:** Heuristic-based Outlier Detection

## 🏗 System Architecture
1. **Producer (`stream_producer.py`):** Simulates a live transaction stream with sub-second latency.
2. **Analytics Engine (`analytics_engine.py`):** Performs real-time feature engineering (calculating moving averages) and monitors price volatility.
3. **Alerting System:** Triggers heuristic alerts when a transaction price deviates significantly from historical product averages.

## 🚀 Key Features
- **Low Latency:** Optimized for near-instantaneous processing of incoming data packets.
- **Dynamic Feature Engineering:** Computes rolling averages on-the-fly to establish "normal" price baselines.
- **Automated Anomaly Detection:** Heuristic logic flags potential errors or fraudulent activity based on a 50% threshold.

## 📊 Business Impact
- **Operational Intelligence:** Reduces the time-to-insight from hours (batch) to seconds (real-time).
- **Risk Mitigation:** Identifies pricing errors or fraudulent entries before they impact the bottom line.
- **Scalability:** Built on a modular OOP structure, allowing for easy integration with Kafka or cloud-based storage like Snowflake.

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/ks-95/Real-Time-Sales-Pipeline.git](https://github.com/ks-95/Real-Time-Sales-Pipeline.git)
2. Install dependencies:
   ```bash
   pip install pandas numpy
3. Run the pipeline:
   ```bash
   python stream_producer.py
