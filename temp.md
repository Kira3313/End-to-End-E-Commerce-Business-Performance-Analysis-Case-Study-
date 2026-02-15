# 📊 End-to-End E-Commerce Business Performance Analysis [Case-Study]

End-to-end exploratory and business performance analysis of an e-commerce dataset using Python (Pandas, NumPy, Matplotlib) and business logic.

---

## 📌 Project Overview

This project analyzes revenue performance, customer behavior, logistics efficiency, and geographic concentration to derive actionable business insights.

Key focus areas:
- Revenue growth & concentration
- Customer retention
- Delivery performance
- Geographic revenue distribution
- Revenue realization efficiency

---

# 📈 Revenue & Growth Analysis

## 🔹 Monthly Revenue Trend & MoM Growth

### 📊 Insight
Revenue demonstrates consistent growth with identifiable seasonal spikes. Early volatility stabilizes over time, indicating increasing business maturity and operational scaling.

Month-over-Month (MoM) analysis reveals natural expansion cycles followed by stabilization phases.

### 💡 Strategic Implication
Seasonal peaks present opportunities for targeted promotions and inventory optimization.

#### 📈 Monthly revenue Vs MOM Growth trend
![MOM Growth Trend](/Visuals/Monthly%20revenue%20vs%20MOM%20growth.png)

---

## 🔹 Average Order Value (AOV)

### 📊 Insight
Average Order Value (AOV) ≈ **160.57 BRL**, representing average revenue per completed transaction (including freight).

### 💡 Strategic Implication
Increasing AOV via bundling, cross-selling, and upselling can directly improve total revenue without increasing acquisition cost.


---

## 🔹 Revenue Concentration (80/20 Pareto Anakysis)

### 📊 Insight
Top 20% of customers contribute approximately **54% of total revenue**, indicating moderate revenue concentration.

Revenue is not overly dependent on a single customer segment but remains influenced by high-value buyers.

### 💡 Strategic Implication
- Strengthen retention strategies for high-value customers  
- Develop mid-tier customers into high-value segments  
- Maintain diversified acquisition efforts  

#### ⚖️ Pareto Analysis (80/20 rule)
![Pareto Analysis](/Visuals/Pareto%20Effect.png)

---

# 👥 Customer Behavior Analysis

## 🔹 Repeat Purchase Rate

### 📊 Insight
Repeat Purchase Rate ≈ **3.12%**, indicating low customer retention and reliance on new customer acquisition.

### 💡 Strategic Implication
- Implement loyalty programs  
- Improve post-purchase engagement  
- Optimize customer experience to increase retention  

---

# 🚚 Logistics & Fulfillment Analysis

## 🔹 Average Delivery Time

### 📊 Insight
Average delivery time ≈ **12.09 days**, indicating moderate logistics efficiency.

While not critically high, delivery speed may impact customer satisfaction in competitive markets.

### 💡 Strategic Implication
- Optimize carrier partnerships  
- Analyze delivery outliers  
- Improve operational bottlenecks  

---

## 🔹 Percentage of Orders Delivered Late

### 📊 Insight
Approximately **8.11%** of delivered orders were late, indicating generally reliable fulfillment performance.

### 💡 Strategic Implication
- Monitor delay drivers (carrier, region, peak periods)  
- Strengthen logistics coordination  
- Enhance customer communication for delayed shipments  

---

## 🔹 Late Delivery Percentage by State

### 📊 Insight
Late delivery rates vary by geography. Some lower-volume states exhibit higher delay percentages, while major revenue-driving states maintain relatively stable performance.

This suggests region-specific logistics inefficiencies.

### 💡 Strategic Implication
- Prioritize high-volume states to protect core revenue  
- Investigate structural causes in high-delay regions  
- Optimize performance based on both delay rate and order volume  

#### 📉 Late delivery rate projection by states
![Late delivery rate by state](/Visuals/Late%20delivery%20by%20states.png)

---

# 🌍 Geographic Revenue Analysis

## 🔹 Top 10 Revenue-Generating States

### 📊 Insight
Revenue is concentrated in major economic hubs, with **São Paulo (SP)** leading significantly.

Top 10 states contribute a substantial share of total revenue, indicating geographic concentration.

### 💡 Strategic Implication
- Maintain dominance in high-performing states  
- Replicate successful strategies in emerging regions  
- Diversify geographic revenue sources to reduce risk  

#### 📉 Revenue concentration among top states
![Revenue Concentration](/Visuals/Revenue%20by%20states.png)

---

# 💰 Revenue Realization & Operational Impact

## 🔹 Total Revenue

**Total Revenue:** 15,843,553 BRL  

---

## 🔹 Revenue from Delivered Orders

- Revenue from Delivered Orders: **15,419,773 BRL**  
- Revenue Realized: **97.3%**  
- Revenue Lost (Non-Delivered): 423,780 BRL (2.7%)

### 📊 Insight
The business captures nearly all potential revenue through successful deliveries. Revenue leakage due to cancellations or non-delivery is minimal.

### 💡 Strategic Implication
Maintain fulfillment efficiency while monitoring cancellation patterns to prevent operational risk.

---

# 🛠 Tools & Technologies Used

- Python (Pandas, NumPy)
- Matplotlib / Seaborn
- SQL-based analytical logic
- Data Cleaning & Transformation
- Jupyter Notebook
- Exploratory Data Analysis (EDA)

---

# 📌 Key Takeaways

- Revenue growth is stable with seasonal expansion patterns.
- Revenue concentration exists but is not excessively dependent on a small segment.
- Customer retention is a primary improvement opportunity.
- Logistics performance is generally strong, with localized inefficiencies.
- 97.3% revenue realization indicates operational robustness.

---

# 🚀 Conclusion

This analysis demonstrates the ability to:

- Perform multi-table joins and data transformations  
- Apply aggregation at correct analytical grain  
- Validate metrics statistically (weighted vs simple averages)  
- Translate technical results into business insights  

The project reflects end-to-end analytical capability from raw data to strategic recommendation.
