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

## Project Structure

The project adheres to a standardized structure to ensure reproducibility, maintainability, and scalability:

credit-risk-model/ <br>
├── .github/workflows/ci.yml # CI/CD pipeline configuration <br>
├── data/ # Data folder (excluded from git) <br>
│ ├── raw/ # Raw dataset (e.g., data.csv) <br>
│ └── processed/ # Processed data for model training <br>
├── notebooks/ <br>
│ └── 1.0-eda.ipynb # Exploratory Data Analysis notebook <br>
├── src/ <br>
│ ├── **init**.py # Package initialization <br>
│ ├── data_processing.py # Feature engineering and preprocessing <br>
│ ├── train.py # Model training and MLflow tracking <br>
│ ├── predict.py # Inference script <br>
│ └── api/ <br>
│ ├── main.py # FastAPI application for model serving <br>
│ └── pydantic_models.py # Pydantic models for API validation <br>
├── tests/ <br>
│ └── test_data_processing.py # Unit tests for data processing <br>
├── Dockerfile # Docker configuration for API <br>
├── docker-compose.yml # Docker Compose for local deployment <br>
├── requirements.txt # Project dependencies <br>
├── .gitignore # Git ignore file <br>
└── README.md # Project documentation <br>
<br>

## etup Instructions

### Prerequisites

Python 3.13.1 <br>
numpy 2.3.1 <br>
pandas 2.3.0 <br>
pip 25.1.1 <br>
scipy 1.16.0 <br>
seaborn 0.13.2 <br>
smatplotlib 3.10.3 <br>
scikit-learn 1.7.0 <br>
