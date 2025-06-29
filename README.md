# credit-risk-modeling

## Overview

This project focuses on developing a credit scoring model to assess and manage credit risk effectively. The model aims to predict the likelihood of borrower default, aligning with regulatory requirements such as the Basel II Capital Accord, while addressing data constraints and balancing interpretability with predictive performance.

## Credit Scoring Business Understanding

The development of a credit scoring model is a critical component of credit risk management, influenced by regulatory frameworks, data constraints, and the need for interpretability in a financial context. Below, we address three key questions to elucidate the business considerations for building an effective credit scoring model.

## Influence of Basel II Accord on Risk Measurement

The Basel II Capital Accord emphasizes robust risk measurement and management practices to ensure financial institutions maintain adequate capital reserves against credit risk. It mandates the use of standardized or internal ratings-based approaches to quantify credit risk, requiring models to be transparent, well-documented, and interpretable. This regulatory framework drives the need for credit scoring models that not only predict risk accurately but also provide clear rationales for their predictions. An interpretable and well-documented model facilitates compliance with regulatory audits, enables stakeholders to understand risk drivers, and supports consistent decision-making, thereby aligning with Basel II’s focus on risk sensitivity and governance.

## Necessity and Risks of Using a Proxy Variable for Default

In the absence of a direct "default" label, creating a proxy variable—such as late payments, missed payments, or high credit utilization is necessary to estimate credit risk. This proxy serves as a substitute to infer the likelihood of default based on observable borrower behaviors. However, relying on a proxy introduces potential business risks. Inaccurate or poorly chosen proxies may misrepresent true default risk, leading to flawed predictions and suboptimal lending decisions. For example, a proxy based solely on payment delays may overlook other risk indicators, such as sudden changes in credit usage. This could result in increased defaults, financial losses, or overly conservative lending practices that exclude creditworthy borrowers, impacting profitability and customer relationships.

## Trade-offs Between Simple and Complex Models

In a regulated financial context, choosing between a simple, interpretable model like Logistic Regression with Weight of Evidence (WoE) and a complex, high-performance model like Gradient Boosting involves key trade-offs. Simple models offer transparency, ease of implementation, and regulatory compliance due to their straightforward logic, making them easier to explain to auditors and stakeholders. However, they may sacrifice predictive power, potentially underfitting complex patterns in data. Conversely, complex models like Gradient Boosting excel at capturing intricate relationships, improving predictive accuracy. Yet, their "black-box" nature complicates interpretability, posing challenges for regulatory scrutiny and stakeholder trust. In a regulated environment, the preference often leans toward simpler models to meet Basel II’s transparency requirements, but hybrid approaches or ensemble methods with explainability tools (e.g., SHAP values) may balance performance and interpretability, depending on institutional priorities.
