import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image

st.header("User car search and Analysis Tool")

car = st.selectbox("Insert brand", ["Audi", "Bentley", "BMW", "Chevrolet","Daewoo","Ford","Honda","Hyundai",
                              "Isuzu","Jeep","Kia", "Landrover","Lexus","Mazda","Mercedes_Benz","MG","Mini","Mitsubishi",
                              "Nissan","Peugeot","Porsche","Subaru","Suzuki","Toyota","Vinfast","Volkswagen","Volvo"])

url = f"https://bonbanh.com/oto/{car}/"

res = requests.get(url)

brand = BeautifulSoup(res.content, "html.parser")

cars = brand.find_all("li", class_=["car-item row1", "car-item row2"] )

for car in cars:
    with st.container():
        st.write("---")
        model = car.find("div", class_="cb2_02").text
        st.success(model)
        left_column, right_column = st.columns(2)
        with right_column:
            status = car.find("div", class_="cb1").text
            price = car.find("div", class_="cb3").text
            location = car.find("div", "cb4").text
            discript = car.find("div", class_="cb6_02").text
            contact = car.find("div", class_="cb7").text
            st.write(status)
            st.write(price)
            st.write(location) 
            st.write(discript)
            st.write(contact)
        with left_column:
            car_img = car.find('div', class_="cb5")
            car_img = car.find('img')
            car_img = car_img.get('src') 
            st.image(car_img)
