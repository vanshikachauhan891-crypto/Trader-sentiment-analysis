# 📊 Trader Sentiment Analysis

## 🔍 Overview

This project analyzes the relationship between **Bitcoin market sentiment (Fear vs Greed)** and **trader performance** using real trading data.

---

## ⚙️ Methodology

* Cleaned and merged sentiment and trading datasets
* Converted timestamps to daily level
* Created key metrics:

  * Daily PnL
  * Win rate
  * Trade frequency
  * Position size
* Performed analysis based on sentiment (Fear vs Greed)
* Segmented traders into behavioral groups

---

## 📈 Key Insights

* Traders perform better during **Greed periods** (higher PnL & win rate)
* Trading activity increases during **Fear periods**, indicating reactive behavior
* Frequent traders show more stable performance than infrequent traders

---

## 💡 Strategy Recommendations

1. Reduce risk exposure during Fear periods due to higher volatility
2. Increase trading activity selectively during Greed periods
3. Frequent traders can adopt more aggressive strategies compared to inconsistent traders

---

## 🚀 How to Run

### Run Notebook

Open `notebook.ipynb` in Jupyter or Google Colab

### Run Dashboard

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Dashboard

The Streamlit dashboard provides:

* PnL comparison by sentiment
* Trade frequency analysis
* Interactive exploration of trading behavior

---

## 📁 Files Included

* `notebook.ipynb` → Full analysis
* `app.py` → Streamlit dashboard
* `merged.csv` → Processed dataset
* `outputs/` → Charts and visuals
