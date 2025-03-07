import streamlit as st
import requests



st.markdown('''
NY Taxi Fare Calculator
''')


date = st.date_input("Pick a date:", format="YYYY/MM/DD")
time = st.time_input("Pick a time:", )

pick_lat = st.slider("Pickup Latitude:", min_value=40.0, max_value=45.0, step=0.001,format="%f")
pick_lon = st.slider("Pickup Longitude:", min_value=-80.0, max_value=-72.0, step=0.001,format="%f")
drop_lat = st.slider("Dropoff Latitude:", min_value=40.0, max_value=45.0, step=0.001,format="%f")
drop_lon = st.slider("Dropoff Longitude:", min_value=-80.0, max_value=-72.0, step=0.001,format="%f")
pass_count = st.slider("Passenger count:",1,6,1)

datetime = f"{date} {time}"

params={
    "pickup_datetime": datetime,
    "pickup_latitude": pick_lat,
    "pickup_longitude": pick_lon,
    "dropoff_latitude": drop_lat,
    "dropoff_longitude": drop_lon,
    "passenger_count": pass_count
}

#st.write(type(datetime.__str__))

if st.button("Get the price", type="primary"):
    url = 'http://taxifare.ckna.net:8333/predict?'

    #url = url + "pickup_datetime=" + str(date) + "+" + str(time) + "&pickup_longitude=" + str(pick_lon) + "&pickup_latitude=" + str(pick_lat) + "&dropoff_longitude=" + str(drop_lon) + "&dropoff_latitude=" + str(drop_lat) + "&passenger_count=" + str(pass_count)

    if url == 'https://taxifare.lewagon.ai/predict':
        st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

    response = requests.get(url, params=params).json()


    #st.write(response)
    st.write(f"USD {round(response['fare'],2)}")
