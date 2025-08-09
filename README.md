<!-- PROJECT BANNER -->
<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning%20Projects-%F0%9F%A4%96-blue?style=for-the-badge" alt="ML Projects">
</p>

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/github/last-commit/nikhilScripts/Machine-learning?color=green&style=flat-square">
  <img src="https://img.shields.io/github/repo-size/nikhilScripts/Machine-learning?color=orange&style=flat-square">
  <img src="https://img.shields.io/github/stars/nikhilScripts/Machine-learning?style=social">
</p>

<h1 align="center">📚 Machine Learning Projects & Deep Learning Modules</h1>

<p align="center">
A curated collection of Machine Learning, PyTorch, Neural Networks, and RNN projects built step-by-step.<br>
Includes real datasets, Kaggle competitions, and end-to-end model training workflows.
</p>

---

## 📌 Table of Contents
- [Module 2 — Classical ML](#module-2--classical-ml)
- [Module 3 — PyTorch Fundamentals](#module-3--pytorch-fundamentals)
- [Module 4 — Neural Networks](#module-4--neural-networks)
- [Module 5 — Deep Learning (RNN)](#module-5--deep-learning-rnn)
- [Setup & Installation](#setup--installation)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)

---

## Module 2 — Classical ML
<details>
<summary>Click to expand</summary>

### 📂 Projects
- **Heart Disease Prediction**  
  Logistic Regression, SVM, Random Forest with precision/recall metrics.  
  Dataset: *[Kaggle Link](https://www.kaggle.com/datasets)*

- **Loan Prediction**  
  Credit default classification with GridSearchCV.

- **Big Mart Sales**  
  Regression task predicting sales based on store/item features.

- **Breast Cancer Prediction**  
  Binary classification using k-fold cross-validation.

### 🛠 Concepts
- Linear Regression
- Logistic Regression
- Support Vector Machines
- Lasso Regression
- K-Fold Cross Validation
- Grid & Random Search
- Model Selection
- Precision, Recall, F1 Score

</details>

---

## Module 3 — PyTorch Fundamentals
<details>
<summary>Click to expand</summary>

- Working with **Tensors** (indexing, slicing, operations)
- PyTorch ↔ NumPy interoperability
- Training loop workflow (`Dataset`, `DataLoader`, `Model`, `Loss`, `Optimizer`)
- Using **CPU vs GPU** with `torch.device`

</details>

---

## Module 4 — Neural Networks
<details>
<summary>Click to expand</summary>

- Building models from scratch
- Activation functions (ReLU, Sigmoid, Tanh, Softmax)
- Multiclass classification
- Convolutional Neural Networks (CNN)
- Data augmentation with `torchvision`
- Saving & loading models (`torch.save` / `torch.load`)

</details>

---

## Module 5 — Deep Learning (RNN)
<details>
<summary>Click to expand</summary>

- RNN fundamentals (hidden states, sequences)
- Character-level classification  
  **Example:** Classifying names by origin using `nn.RNN` / `nn.LSTM`

</details>

---

## ⚙ Setup & Installation
```bash
git clone https://github.com/nikhilScripts/Machine-learning.git
cd Machine-learning
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
