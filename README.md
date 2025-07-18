# 🍲 Data-Driven Trend Adoption for African Restaurants: A Case Study on Amala in the UK

This project explores how **Nigerian food trends—specifically *Amala***—are surfacing in the UK, using **Google Trends time-series analysis** to guide strategic decisions for small African food businesses. It supports a case study of *Amala Hut*, a Nigerian restaurant planning to expand into the UK, and addresses how to detect trends and recommend business adoption strategies.

---

## 🌍 Background

As African cuisine gains global popularity, small African-owned food businesses face key questions:

> *Which traditional meals are trending abroad? Should we expand our offering based on search and cultural demand data?*

This research draws inspiration from data-driven product strategies used in industries like tech and applies a similar method to **retail food trends**. Just like audio brands use reviews and consumer data to guide product launches, African restaurants can now do the same with **cuisine trends**.

---

## 🧩 Problem Statement

In the multicultural and competitive UK restaurant scene, identifying which **West African dishes are gaining popularity** is critical for small businesses. However, unstructured or anecdotal evidence makes it difficult to justify strategic decisions. This project seeks to answer:

> *Is Amala trending enough in the UK for a small African restaurant to adopt or expand its offering?*

---

## 🎯 Objectives

- Scrape and analyze UK-based Google search interest for Amala and other Nigerian dishes.
- Calculate **trend metrics**:
  - **Velocity** (growth rate)
  - **Acceleration** (momentum)
  - **Volatility** (stability)
- Create a **trendiness score** for each dish to support business decisions.
- Recommend whether *Amala Hut* should include Amala on their menu in the UK.

---

## 🧠 Methodology

- Time-series analysis of Google Trends data across multiple months
- Compute trend signals using:
  - `.diff()` for velocity
  - `.diff()` of velocity for acceleration
  - `rolling().std()` for volatility
- Normalize these scores and combine into a **composite trendiness score**
- Simulate business-level decision-making using **cost**, **local relevance**, and **trend strength**

---

## 🗃️ Data Sources

- **Google Trends** via the `pytrends` Python API
- Keywords: `"Amala"`, `"Pounded yam"`, `"Jollof rice"` (optional comparisons)
- Focus: UK region, last 5 years

---

## 🛠️ Tools Used

- Python (Jupyter Notebook)
- Pandas, NumPy
- Pytrends (Google Trends API wrapper)
- Matplotlib, Seaborn
- Scikit-learn (for scaling and model setup)
- Markdown for documentation

---

## 📈 Business Recommendations:

Jollof Rice is the most trend-responsive dish and should be prioritized for adoption.  
Amala is stable and suitable for culturally aligned markets, while Pounded Yam may be deferred unless niche demand justifies it.

---

## 🗂️ Project Structure.
.

├── data/ Raw and cleaned Google Trends data

├── notebooks/ Jupyter Notebooks for trend analysis and scoring

├── scripts/ pytrends-based scraper

├── reports/ Business recommendation report

├── docs/ Project documentation (Markdown or Sphinx-ready)

---

## 📌 Deliverables

- **Trend detection notebook** (with visualizations, rolling averages, trendiness score)
- **Summarized report** on whether *Amala Hut* should adopt Amala based on data
- **Documentation** of entire research pipeline and model logic