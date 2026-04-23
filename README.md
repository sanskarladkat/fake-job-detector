# 🧠 Fake Job Detector

A machine learning-powered web application that detects suspicious and fake job postings in real-time using advanced NLP and classification techniques.

## ✨ Features

- **Real-time Detection**: Instantly analyze job postings and get risk assessment
- **Probability Scoring**: Get confidence scores for fake job predictions
- **Risk Classification**: Three-tier risk level system (LOW ✅, MEDIUM ⚠️, HIGH ⚠️)
- **Text Analysis**: Intelligent keyword detection and text feature engineering
- **Interactive Web UI**: User-friendly Streamlit interface for easy analysis
- **Contributor Leaderboard**: Track and celebrate community contributions

## 🔧 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web framework
- **Machine Learning**: Scikit-learn - Classification models
- **NLP**: TF-IDF vectorization for text processing
- **Data Processing**: Pandas, NumPy, SciPy
- **CI/CD**: GitHub Actions - Automated leaderboard updates
- **Data**: Fake job postings dataset

## 📋 Prerequisites

- Python 3.8+
- pip or conda

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fake-job-detector.git
   cd fake-job-detector
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Run the Web Application

```bash
streamlit run app/app.py
```

The application will open at `http://localhost:8501` in your browser.

### Using the Interface

1. Enter a **Job Title** in the sidebar
2. Paste the **Job Description**
3. Add any **Requirements**
4. Click the **🔍 Analyze Job** button
5. View the prediction results with risk level and probability score

### Using the Prediction Module

```python
from src.predict import predict_job

text = "Your job posting text here"
probability, risk_level = predict_job(text)

print(f"Fake Probability: {probability * 100:.2f}%")
print(f"Risk Level: {risk_level}")
```

## 📊 Project Structure

```
fake-job-detector/
├── app/
│   └── app.py                          # Main Streamlit application
├── src/
│   └── predict.py                      # Prediction engine
├── models/
│   ├── model.pkl                       # Trained ML model
│   └── tfidf.pkl                       # TF-IDF vectorizer
├── data/
│   └── fake_job_postings.csv          # Training dataset
├── notebooks/
│   └── eda.ipynb                       # Exploratory Data Analysis
├── leaderboard/
│   ├── leaderboard.csv                 # Contributor rankings
│   └── update-leaderboard.yml          # GitHub Actions workflow
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## 🤖 How It Works

### Text Processing
- Converts text to lowercase and removes special characters
- Applies TF-IDF vectorization for feature extraction

### Feature Engineering
- **Text Length**: Length of processed text
- **Word Count**: Number of words in the text
- **Suspicious Keywords**: Detects phrases like "urgent", "quick money", "no experience", "work from home"

### Prediction
- Combines TF-IDF features with engineered features
- Uses trained machine learning model
- Returns probability score and risk classification:
  - **HIGH** (⚠️): Probability > 70%
  - **MEDIUM** (⚠️): Probability > 40%
  - **LOW** (✅): Probability ≤ 40%

## 📈 Exploratory Data Analysis

Check out [notebooks/eda.ipynb](notebooks/eda.ipynb) for detailed analysis of:
- Dataset characteristics
- Feature distributions
- Class imbalance analysis
- Text patterns in fake vs. legitimate jobs

## 🏆 Leaderboard

Our community contributions are tracked on the [leaderboard](leaderboard/leaderboard.csv)! Every PR automatically updates the ranking.

### How to Join the Leaderboard
1. Make improvements to the project
2. Submit a Pull Request
3. Our GitHub Actions workflow will automatically add you upon merge

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** and commit: `git commit -m "Add your message"`
4. **Push to your fork**: `git push origin feature/your-feature-name`
5. **Open a Pull Request**

### Contribution Ideas
- Improve model accuracy
- Add new features to the web interface
- Enhance text processing
- Add more suspicious keywords
- Improve documentation
- Add unit tests

### Automated Workflow
When you open a PR, the GitHub Actions workflow will:
- Verify your contribution
- Update the contributor leaderboard
- Add a welcome comment to your PR

## 📝 Requirements

Key dependencies:
- `streamlit` - Web framework
- `scikit-learn` - ML models
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `scipy` - Scientific computing
- `pickle` - Model serialization

## 🐛 Known Issues & Limitations

- Model performance depends on training dataset quality
- Limited to English language text
- May have false positives/negatives with edge cases
- Requires pre-trained model files in `models/` directory

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♀️ Support

Have questions or found a bug? Please:
- Open an [Issue](https://github.com/your-username/fake-job-detector/issues)
- Check existing issues for similar problems
- Provide detailed information about your problem

## 🎯 Future Enhancements

- [ ] Multi-language support
- [ ] Advanced ML model architectures (LSTM, BERT)
- [ ] Real-time web scraping integration
- [ ] API endpoint for programmatic access
- [ ] Enhanced explanation of prediction reasons
- [ ] User feedback mechanism for model improvement
- [ ] Batch processing for multiple job postings
- [ ] Historical analysis and trend detection

## 👥 Contributors

Thanks to everyone contributing to this project! 🙌

---

**Made with ❤️ by the community**
