# **Predicting Customer Retention in E-Commerce**

**BUS 32130: Data Visualization for Decision-Making \- Final Project**

### **📊 [Link to Tableau Dashboard](http://docs.google.com/Insert_Your_Tableau_Public_Link_Here)**

## **Executive Summary**

In e-commerce, unlike subscription-based models, online retailers rarely have a clear "cancellation" point. Customer retention must instead be inferred directly from purchasing behavior. This project explores the early purchasing signals that indicate whether a customer is likely to return and generate long-term value.

This analytical dashboard is designed to help businesses move beyond simple top-line metrics and uncover the behavioral drivers of customer loyalty.

## **Target Audience & Business Questions**

**Target Audience:** E-commerce Strategy, CRM, and Marketing Teams.

These stakeholders need to identify which early customer behaviors suggest stronger retention potential to optimize customer segmentation, trigger targeted follow-up campaigns, and allocate retention budgets effectively.

**Core Questions Answered:**

1. Do customers with higher initial purchase values exhibit higher repeat purchase rates?  
2. Does purchasing a wider variety of products in the first order indicate stronger future engagement?  
3. How quickly do repeat customers usually make their second purchase, and how does that velocity impact overall lifetime value?

## **Hypotheses**

Our visual analysis was guided by three core hypotheses:

* **Hypothesis 1 (Spend):** Customers with a higher total value on their very first purchase are significantly more likely to become repeat customers.  
* **Hypothesis 2 (Basket Size/Variety):** Customers who purchase a wider variety of distinct products in their initial order are more likely to return.  
* **Hypothesis 3 (Velocity):** A shorter time gap between a customer’s first and second purchase strongly correlates with higher long-term expected value.

## **Data Processing & Cleaning**

To ensure the integrity of the analysis, the raw transactional dataset underwent rigorous cleaning and preparation before visualization:

1. **Handling Missing Data:** Removed records with missing CustomerID values, as anonymous transactions cannot be tracked longitudinally for retention analysis.  
2. **Addressing Anomalies:** Filtered out records with negative Quantity values and zero/negative UnitPrice values. These typically represent returns, cancellations, or pricing errors and would distort revenue and first-purchase baseline calculations.  
3. **Feature Engineering:** Created a Transaction Value field by multiplying Quantity by UnitPrice.  
4. **Data Aggregation:** The raw data was structured at the line-item level. We aggregated this data first to the transaction level (using InvoiceNo) and then to the customer level (using CustomerID) to create our primary analytical metrics: *First Purchase Value*, *Total Customer Value*, *Purchase Frequency*, *First Basket Variety*, and *Time to Second Purchase*.

## **Assumptions**

* **Defining Retention:** Because there is no formal account cancellation data, customer retention is strictly measured through repeat purchasing behavior. A "repeat customer" is defined as any CustomerID associated with more than one unique InvoiceNo on separate dates.  
* **First Purchase Metrics:** First purchase value and basket variety are calculated strictly from the customer’s earliest chronological transaction date.  
* **Outlier Handling:** Very high first-purchase values and massive basket sizes were assumed to represent wholesale-style B2B buyers or unusually large edge cases. These segments were grouped separately ("20k+") to avoid skewing standard consumer trends.

## **Limitations**

* **Correlation vs. Causation:** This analysis identifies behavioral patterns and associations, but it cannot prove causation. For example, while we observe that customers who return sooner generate higher lifetime value, we cannot confirm if this is organic behavior or the result of a specific post-purchase marketing campaign.  
* **Missing Contextual Data:** The dataset lacks customer demographics, marketing campaign exposure, website browsing activity, acquisition channels, and profit margins.  
* **Sample Sizes at Extremes:** Some of the highest-value customer cohorts contain a relatively small number of total customers; trends in these extreme upper bounds should be interpreted directionally rather than as absolute rules.

## **AI / LLM Usage Statement**

*As per course requirements, the following details the use of AI/LLMs in this project:*

LLM tools (ChatGPT / Gemini) were utilized in a limited capacity during the early ideation phase to brainstorm project directions, structure the business problem, and refine the wording of our hypotheses. AI was also used to help format this README.md file. All actual data cleaning, dashboard calculations, visual design, and analytical execution were performed manually using Tableau and the raw dataset.
