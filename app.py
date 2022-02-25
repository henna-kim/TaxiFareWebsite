import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


# date and time
d = st.date_input(
    "What date do you want to see?",
    datetime.date(2019, 7, 6))

t = st.time_input('What time do you want to see?', datetime.time(8, 45))

st.write('The date is:', d), st.write('Time is', t)

# pickup longitude
pickup_longitude = st.number_input('Insert a pickup longitude')
st.write('The pickup longitude is ', pickup_longitude)

# pickup latitude
pickup_latitude = st.number_input('Insert a pickup latitude')
st.write('The pickup latitude is ', pickup_latitude)

# dropoff longitude
dropoff_longitude = st.number_input('Insert a dropoff longitude')
st.write('The dropoff longitude is ', dropoff_longitude)

# pickup latitude
dropoff_latitude = st.number_input('Insert a dropoff_latitude')
st.write('The dropoff latitude is ', dropoff_latitude)

# passenger count
number = st.number_input('Insert the number of passengers')
st.write('The number of passengers are ', number)


'''
# Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
if st.button('click me'):
    # print is visible in the server output, not in the page
    url = 'https://taxifare.lewagon.ai/predict'

    if url == 'https://taxifare.lewagon.ai/predict':

        st.markdown(
            'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

    # Let's build a dictionary containing the parameters for our API...

    api_dict = {'pickup_datetime': f"{d} {t}",
                'pickup_longitude': pickup_longitude,
                'pickup_latitude': pickup_latitude,
                'dropoff_longitude': dropoff_longitude,
                'dropoff_latitude': float(dropoff_latitude),
                'passenger_count': int(number)}

    # Let's call our API using the `requests` package...
    r = requests.get(url, params=api_dict)

    # Let's retrieve the prediction from the ** JSON ** returned by the API...
    # st.text(r['fare'])
    st.text(round(r.json()['fare'], 2))

    # Finally, we can display the prediction to the user

    print('button clicked!')
    # st.write('I was clicked 🎉')
    # st.write('Further clicks are not visible but are executed')
else:
    st.write('I was not clicked, please click again 😞')
