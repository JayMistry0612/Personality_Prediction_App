# Personality Prediction App

This project is a machine learning web application that predicts personality traits based on user input. It uses a Decision Tree Classifier trained on a custom dataset and is deployed using Streamlit.

## Project Structure

- **Model.ipynb.ipynb**: Jupyter notebook for data preprocessing, model training, and exporting the trained pipeline as `pipe.pkl`.
- **Personality_prediction.py**: Streamlit app for user interaction and prediction.
- **pipe.pkl**: Serialized machine learning pipeline used by the Streamlit app.
- **requirements.txt**: List of Python dependencies.

## How It Works

1. **Data Preparation & Model Training**  
   - The notebook loads and preprocesses the dataset (`personality_dataset (1).csv`).
   - Handles missing values, encodes categorical features, scales data, selects features, and trains a Decision Tree Classifier.
   - The trained pipeline is saved as `pipe.pkl` using pickle.

2. **Web Application**  
   - The Streamlit app (`Personality_prediction.py`) loads the trained model.
   - Users enter their data through a simple web form.
   - The app predicts and displays the personality trait.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/JayMistry0612/Personality_Prediction_App.git
cd Personality_Prediction_App
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the Model

- Run `Model.ipynb.ipynb` to train the model and generate `pipe.pkl`.
- Ensure `pipe.pkl` is in the same directory as `Personality_prediction.py`.

### 4. Run the Streamlit App

```bash
streamlit run Personality_prediction.py
```

## Deployment

You can deploy this app for free using [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code (including `pipe.pkl` and `requirements.txt`) to a public GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. Set `Personality_prediction.py` as the main file.
4. Deploy!

## Example Input Fields

- Time_spent_alone(Number)
- Stage_fear (Yes/No)
- Social_event_attendance(Number)
- Going_out(Number)
- Drained_after_socializing (Yes/No)
- Friends_circle_size(Number)
- Post_frequency(Number)

## Requirements

- Python 3.7+
- streamlit
- scikit-learn
- pandas
- numpy
- matplotlib

## License

This project is for educational purposes.
