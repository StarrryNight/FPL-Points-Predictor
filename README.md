# FPL Points Predictor ⚽📊

A machine learning-based Fantasy Premier League (FPL) points prediction system that uses historical gameweek data to forecast player performance and help optimize team selections.

## 🎯 Overview

This project uses linear regression throug SKLearn to predict FPL player points based on various performance metrics including expected goals (xG), assists, clean sheets, minutes played, and other key statistics. The system processes historical gameweek data to train a linear regression model that can forecast future player performance.

## ✨ Features

- **Data-Driven Predictions**: Uses comprehensive FPL statistics including xG, assists, clean sheets, and more
- **Historical Analysis**: Processes multiple gameweek datasets for robust model training
- **Performance Visualization**: Interactive scatter plots showing prediction accuracy
- **Data Cleaning**: Automated handling of player transfers, injuries, and data inconsistencies
- **Model Evaluation**: R² score calculation to measure prediction accuracy

## 🛠️ Libraries

- **Python 3.x**
- **Pandas** 
- **Scikit-learn**
- **Seaborn** 
- **Matplotlib** 
- **NumPy** 

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/FPL-Points-Predictor.git
   cd FPL-Points-Predictor
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   PLEASE
   ```bash
   pip install pandas scikit-learn seaborn matplotlib numpy 
   ```
    and also 

   ```bash
   pip install PyQt6
   ```
   for plotting.

## 🚀 Usage

### Basic Usage

Run the main prediction script:

```bash
python main.py
```

### Configuration

Modify the following parameters in `main.py`:

- `using_week`: The gameweek to use for training data
- `target_week`: The gameweek to predict
- `evaluationMetric`: List of features to use for prediction
   - Comment out unwanted metrics to ignore

### Example Configuration

```python
using_week = 15  # Train on gameweek 15 data
target_week = 19  # Predict gameweek 19 performance

evaluationMetric = [
    'xP',          
   # 'minutes',      
    #'assists',      
    'clean_sheets', 
    'expected_goal_involvements',
    #'expected_goals',
    'expected_goals_conceded',
    'starts'
]
```

```

## 🔧 How It Works

1. User chooses data and target on main.py
2. Data sent to cleanup.py for results
2. Recalling y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ, model computes the best fitting coefficients **b** for **n** evaluation metrics using using_week's dataand the points obtained a week after.
3. Coefficients are used to predict points of players in the next gameweek.
4. Data is plotted and R2 is displayed

## 📊 Model Performance

The system evaluates prediction accuracy using:
- **R² Score**: Measures the proportion of variance explained by the model
- **Scatter Plot Visualization**: Shows prediction vs actual performance correlation
- **Player Labeling**: Highlights high-performing players for easy identification

## Results
The highest R2 value obtain through different datasets is only around 0.5, which is far from ideal for accurate prediction.

## ⚠️ Disclaimer

This tool is for educational and entertainment purposes only. FPL predictions are inherently uncertain and should not be used as the sole basis for financial decisions. Always do your own research and consider multiple factors when making FPL team selections.


---

**Happy FPL Managing! 🏆**
