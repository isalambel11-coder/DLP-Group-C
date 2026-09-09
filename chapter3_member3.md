# Chapter 3 – Research Methodology, Development Model and Proposed Architecture

## 3.1 Research Methodology
The proposed study adopts a **Data-driven research approach using CRISP-DM**. This approach is suitable because the literature reviewed in Assignment 1 and Assignment 1B shows a strong use of machine-learning and behavioural-analysis techniques for Data Loss Prevention (DLP), insider-threat detection and data-exfiltration detection. The review also identifies recurring limitations, including reliance on benchmark/synthetic datasets, limited real-time validation and the need to combine behavioural and contextual information.

## 3.2 Development Model
The proposed prototype follows an **Iterative and Incremental development model**. A complete production DLP platform is outside the proposal-stage requirement. Instead, the prototype can be developed in small increments: data preprocessing, feature extraction, detection-model development, alert/risk scoring, and testing. Each increment can be tested before the next component is added.

## 3.3 Justification
CRISP-DM provides a structured sequence for understanding the DLP problem, understanding and preparing data, modelling leakage-related behaviour, evaluating the model and preparing the proposed deployment direction. This matches the Assignment 1B findings that current DLP research increasingly uses machine learning, behavioural and temporal features, while also facing problems with class imbalance, generalisability and real-time deployment. The iterative development model complements CRISP-DM because the proposed technical solution can be refined progressively rather than attempting to build a complete DLP platform at once.

## 3.4 Methodology Phases
1. **Business/Research Understanding** – define the DLP problem, leakage risks, research gap and objectives.
2. **Data Understanding** – identify suitable DLP/insider-threat data and inspect its attributes, classes and quality.
3. **Data Preparation** – clean records, encode categorical values, handle missing values and prepare features.
4. **Modelling** – train and compare suitable machine-learning/anomaly-detection models for suspicious activity.
5. **Evaluation** – assess detection performance using appropriate classification and operational metrics.
6. **Deployment/Prototype Direction** – demonstrate how the selected model could support a DLP monitoring pipeline.

## 3.5 Proposed System Architecture
The proposed architecture is a layered DLP monitoring prototype. Input activity/log data enters the data collection layer. The preprocessing layer cleans and transforms the records. Feature extraction produces behavioural and contextual features. The detection layer applies a machine-learning/anomaly-detection model. The risk/decision layer assigns a normal or suspicious status and can generate an alert. Results are stored for evaluation and reporting.

### Alignment with the literature
The architecture responds directly to the Assignment 1B research gaps: multi-channel/contextual signals are preferred over a single isolated channel; behavioural and temporal information are useful; benchmark-data limitations require careful evaluation; and practical monitoring should consider false positives and processing time.

## 3.6 Proposed Process Flow
Input activity → validation → preprocessing → feature extraction → detection model → risk/decision → alert/log result → evaluation.

## 3.7 Technical Components
- Python
- pandas and NumPy for data preparation
- scikit-learn for baseline machine-learning experiments
- YAML configuration for reproducible settings
- CSV/JSON-compatible activity records
- Detection and evaluation scripts
- Architecture and process-flow diagrams

## 3.8 Preliminary Implementation
The source-code folder contains a small proof-of-concept pipeline. It does not claim to be a completed production DLP system. The code demonstrates the intended technical direction: load activity data, prepare features, train a baseline classifier when labels are available, produce predictions and report basic evaluation metrics.

## 3.9 Link to Assignment 1 and Assignment 1B
Assignment 1 established the Data Loss Prevention research area. Assignment 1B reviewed 48 studies from the 2022–2026 scope and identified recurring themes in ML/DL insider-threat detection, behavioural analysis, cloud/endpoint DLP and data-exfiltration detection. It also identified gaps involving benchmark/synthetic datasets, narrow single-channel approaches, real-time deployability, evasion resistance and privacy. The proposed methodology and architecture are therefore designed as a preliminary, data-driven DLP detection prototype that can later be evaluated against these limitations.
