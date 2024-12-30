import streamlit as st
import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

st.set_page_config(
    page_title="MongoDB Movie Site Demo"
)

st.write("# MongoDB Overview")
st.markdown(
    """
    This simple app connects to a MongoDB Atlas Server
    with a bunch of sample data provided by Mongo. The data
    mocks simple movie information
"""
)

MONGODB_URI = st.secrets["MONGODB_URI"]
# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    st.write("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    st.write(e)

my_filter = {
    "rated": {
        "$nin": ["APPROVED", "Approved", "PASSED","M"]
    },
    "plot": { "$exists": True }
}

#@st.cache_data(ttl=600)
def get_data():
    db = client.sample_mflix
    items = db.movies.find(my_filter).limit(12)
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()
if st.checkbox('Show raw object data'):
    st.subheader('Raw Movie object data')
    st.write(items)


df = pd.DataFrame(items)

if st.checkbox('Show Dataframe Data'):
    st.subheader('Dataframe')
    st.write(df)




rated_counts = df['rated'].value_counts()
st.bar_chart(rated_counts)

cols = st.columns(3)

# Iterate through items and add to columns
for i, item in enumerate(items):
    with cols[i % 3]:  # Cycle through columns (0, 1, 2, 0, 1, 2...)
        with st.container(border=True, height=300):
            if {item['title']} is not None:
                st.write(f"#### {item['title']}")
            if {item['plot']} is not None:
                st.write(f"{item['plot']}")

    if (i + 1) % 3 == 0:  # Add a new row after every 3 items
        st.write("")  # Visual separator (optional)