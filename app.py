import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Fungsi untuk membaca data
def load_data():
    # Gantilah 'path_to_your_data.csv' dengan path yang sesuai dengan file data Anda
    df = pd.read_csv('Copy of brentcrudeoil - dailybrentoil.csv')
    df = df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'], axis=1)
    return df


# Fungsi untuk melatih model dan mengembalikan hasil prediksi
def train_and_predict(df):
    # Pisahkan data menjadi train dan test
    train_size = int(len(df) * 0.8)
    train, test = df[0:train_size], df[train_size:]

    # Pilih fitur dan target
    features = ['Close', 'Low', 'High']
    target = 'chg(close)'

    # Pisahkan data menjadi fitur (X) dan target (y)
    X_train, y_train = train[features], train[target]
    X_test, y_test = test[features], test[target]

    # Inisialisasi model Regresi Linear
    model = LinearRegression()

    # Latih model
    model.fit(X_train, y_train)

    # Lakukan prediksi
    predictions = model.predict(X_test)

    # Evaluasi hasil dengan Mean Squared Error (MSE)
    mse = mean_squared_error(y_test, predictions)
    st.write(f"Mean Squared Error (Linear Regression): {mse}")

    # Plot hasil prediksi
    plt.figure(figsize=(12, 6))
    plt.plot(test['Date'], y_test, label='Actual', marker='o')
    plt.plot(test['Date'], predictions, label='Linear Regression Prediction', marker='o')
    plt.title('Linear Regression Prediction vs Actual')
    plt.xlabel('Date')
    plt.ylabel('chg(close)')
    plt.legend()
    st.pyplot(plt)

# Fungsi utama Streamlit
def main():
    st.title("Time Series Prediction App")
    
    # Load data
    df = load_data()

    # Tampilkan ringkasan data
    st.write("Data Summary:")
    st.write(df.head())

    # Latih model dan tampilkan hasil prediksi
    st.write("Model Training and Prediction:")
    train_and_predict(df)

# Jalankan aplikasi Streamlit
if __name__ == "__main__":
    main()
