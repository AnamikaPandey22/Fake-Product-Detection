# 🧠 Fake Product Detection

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

## 🛠 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/yourusername/Fake-Product-Analyzer.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```

📦 Folder Structure
Fake-Product-Detection/
│
├── yolo_model/            # YOLOv8 weights or model (best.pt)
├── logo_classifier/       # ResNet50 (logo_classifier_image.keras)
├── data/                  # Product dataset and Logo dataset
├── app.py                 # Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # Project overview

---

💡 Future Scope
*Add more brands and logo variants
*Fine-tune classification model on a larger dataset
*Improve explanation quality using better LLM prompting
*Add OCR to read product labels
*Host as a cloud API or mobile app

---

🙋‍♀️ Author
Anamika Pandey
Final Year BCA | CDAC Patna | AI/ML Enthusiast
🌐 [LinkedIn](https://www.linkedin.com/in/anamika-pandey-ana/) | 🧠 [Gmail](anamika221105@gmail.com)

💬 Open to collaborations, ideas, and feedback!
