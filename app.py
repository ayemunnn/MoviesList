import streamlit as st
import pandas as pd





USER_CREDENTIALS = {
    'admin': 'password123',
    'user': '123456',
}

# Function to authenticate the user
def authenticate(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return True
    return False
st.title('Movie Watchlist for Kannu Ji')
st.info("Hey, I hope you will like it! - Yours Truly, Chor")

# Load the locally stored CSV file
movies_data = pd.read_csv('Movie.csv')

# Filter the movies based on input features
selected_genre = st.text_input('Enter Genre')
selected_category = st.text_input('Enter Category')

filtered_movies = movies_data[
    (movies_data['Genre'].str.contains(selected_genre, case=False, na=False)) &
    (movies_data['Category'].str.contains(selected_category, case=False, na=False))
]

# Display the note
st.info("This app isn't fully developed yet, to choose from genre, you can write Drama, War, Horror, Romance, Thriller, Action, Comedy and for Unique Categories: Movie and Web Series")





# Display the filtered movies table
if filtered_movies.empty:
    st.warning("No movies found with the given input features.")
else:
    # Display the table
    st.table(filtered_movies)
