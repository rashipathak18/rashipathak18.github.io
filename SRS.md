# Software Requirements Specification (SRS)
## Sales Performance Dashboard & Analytical System
**Author:** Rashi Pathak  
**Domain:** Retail and E-commerce  
**Assessment Target:** HCL Tech Project Submission / ABES B.Tech Data Analyst Curriculum  
**GitHub Repository:** [https://github.com/rashipathak18/rashipathak18.github.io](https://github.com/rashipathak18/rashipathak18.github.io)  
**Live Application URL:** [https://rashipathak18.github.io](https://rashipathak18.github.io)  

---

## 1. Executive Summary & Purpose
The **Sales Performance Dashboard** is an enterprise data analytics platform designed to analyze, monitor, and visualize retail sales performance across multiple regions, product tiers, and temporal dimensions. It provides end-to-end data processing from ingestion and cleaning in Python to relational Oracle SQL schema modeling, and interactive real-time visual exploration hosted publicly on GitHub Pages.

## 2. GitHub Repository & Live URLs
- **GitHub Repository Link:** [https://github.com/rashipathak18/rashipathak18.github.io](https://github.com/rashipathak18/rashipathak18.github.io)
- **Live Deployed Dashboard:** [https://rashipathak18.github.io](https://rashipathak18.github.io)

## 3. Specification Matrix (ABES / HCL Tech Guidelines Compliance)
| Specification Parameter | Detail & Compliance |
| :--- | :--- |
| **Project No. & Title** | Project 1: Sales Performance Dashboard |
| **Domain** | Retail and e-commerce |
| **Core Technical Focus** | pandas cleaning; Oracle tables, joins, GROUP BY, window functions; Power BI / Web KPI cards, trend and regional charts |
| **Data Source & Verification Approach** | Kaggle retail sales CSV; reconcile row counts and total sales across CSV, Oracle, and Web Dashboard |
| **Key Test Cases** | Null/duplicate rows, negative amounts, date format errors, region slicers |
| **Measurable Acceptance Criteria** | Top 10 products and monthly trend correct; total sales matches source within 0.1%; at least 5 KPIs and 3 slicers |
| **Deliverables** | Problem statement, KPI definitions, ER diagram, Python notebook (.ipynb), Oracle SQL scripts, Web Dashboard, Data-quality report, GitHub repo, Presentation (.pptx) |

## 4. Key Performance Indicators (KPIs)
1. **Total Gross Revenue:** Reconciled sum of all completed transactions (₹1,614,000).
2. **Total Orders:** Total count of unique order IDs (350 orders).
3. **Total Units Sold:** Cumulative sum of quantities sold (1,032 units).
4. **Average Order Value (AOV):** Total Revenue divided by Total Orders (₹4,611.43).
5. **Units per Transaction:** Total Units divided by Total Orders (~2.95 units/order).

## 5. Verification Test Cases & Quality Report
- **TC-01 (Null Value Check):** Zero missing records detected across all primary attributes.
- **TC-02 (Duplicate Handling):** Automated deduplication routine executed.
- **TC-03 (Boundary Validation):** All quantities and unit prices verified > 0.
- **TC-04 (Mathematical Parity):** Total sales mathematically verified (`Revenue == Quantity * Price`).
- **TC-05 (Reconciliation):** Source CSV total matches Python analysis and Web Dashboard within 0.00% variance.

## 6. Deliverable Inventory
- `Sales_Performance_Dashboard.ipynb`: Interactive Jupyter Notebook with complete EDA and visualizations.
- `Software_Requirements_Specification_SRS.docx` & `SRS.md`: Formal requirements specification including GitHub link.
- `Sales_Performance_Dashboard_Presentation.pptx`: Comprehensive project presentation.
- `Sales_Performance_Dashboard_Code.docx`: Complete project source code compilation with page separations.
- `index.html`: Fully interactive GitHub Pages web dashboard.
