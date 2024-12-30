import streamlit as st
import sys
import pymongo
import pandas as pd
import re

st.set_page_config(
    page_title="Retail MongoDB Demonostration Site"
)

st.write("# Retail MongoDB Demonstration")
st.write("Get ready for some retail database fun")

# Access MongoDB credentials from Streamlit secrets
MONGODB_URI = st.secrets["MONGODB_URI"]

# Connect to MongoDB
try:
    client = pymongo.MongoClient(MONGODB_URI)
    db = client.get_database("grocery")  # Replace with your database name
    collection = db["grocery_items"]  # Replace with your collection name
    st.success("Connected to MongoDB!")

except Exception as e:
    st.error(f"Error connecting to MongoDB: {e}")

search = st.text_input("Item Search")

# Now you can interact with your MongoDB database
# For example, to fetch all documents from the collection:
# documents = list(collection.find())
# st.write(documents)
pattern = re.compile(search, re.IGNORECASE)

    # Use the $regex operator to filter documents
my_filter = {
    "$or": [
        {"name": {"$regex": pattern}},
        {"description": {"$regex": pattern}}
    ]
}

st.write("### Standard Regex Filter")
st.write("This is a standard filter in MongoDB searching for items like what was in the searchbar, but has to be literal (not case sensitive) based on either the name or the description.")
if st.checkbox("Show filter"):
    st.write(my_filter)
def get_data():
    db = client.grocery
    items = db.grocery_items.find(my_filter)
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

cols = st.columns(3)

# Iterate through items and add to columns
for i, item in enumerate(items):
    with cols[i % 3]:  # Cycle through columns (0, 1, 2, 0, 1, 2...)
        with st.container(border=True, height=200):
            st.write("### " + item['name'])
            st.write(item['description'])
            st.write("###### Calories: " + str(item['calorie_count']))

    if (i + 1) % 3 == 0:  # Add a new row after every 3 items
        st.write("")  # Visual separator (optional)

st.write("### Vector Search Example")
st.markdown(
    """
    This is a vector search example using the same search keywords typed in above
    also utilizing the built in MongoDB Atlas Vector search capabilities. 
    Overall this is simple to set up and uses simple indexes and a cosine aggregation
    to find nearest neighbor items.
    """
)



client.close()