# 🧠 Fake Product Analyzer

An AI-powered system that detects product logos from images using YOLOv8 and classifies them as Real or Fake using ResNet50. Built as part of my AI/ML project during the CDAC Training Program.
> 🚧 **Status**: This project is still in development. More features and improvements coming soon!

---

## 🔍 Problem Statement

Counterfeit products cause major financial and health-related issues. This project aims to:
- Detect logos from product images
- Classify the logo as *Real* or *Fake*
- Provide explanation or reasoning using an LLM
- Offer an easy-to-use Streamlit interface

---

## 🚀 Tech Stack Used

| Component        | Technology         |
|------------------|--------------------|
| Object Detection | YOLOv8             |
| Image Classifier | ResNet50           |
| LLM Integration  | OpenAI             |
| Frontend         | Streamlit          |
| Language         | Python             |

---

## 🖼 Sample Output

| Input Image | Detected Logo | Classification | Explanation |
|-------------|---------------|----------------|-------------|
| ![input](streamlit_app/sample1.jpg) | Nestle | Fake | The logo font doesn't match official Nestle branding. |

---

## 🛠 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/yourusername/Fake-Product-Analyzer.git
