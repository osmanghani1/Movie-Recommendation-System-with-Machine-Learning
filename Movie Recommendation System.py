#!/usr/bin/env python
# coding: utf-8

# # Importing the dependencies

# In[1]:


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# # Data Collection and Pre_Processing

# In[2]:


movies_data=pd.read_csv("movies.csv")


# In[3]:


movies_data.head()


# In[4]:


movies_data.shape


# In[5]:


selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)


# In[6]:


for feature in selected_features:
       movies_data[feature]=movies_data[feature].fillna('')


# In[7]:


combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']


# In[8]:


print(combined_features)


# In[9]:


vectorizer=TfidfVectorizer()


# In[10]:


feature_vectors=vectorizer.fit_transform(combined_features)


# In[11]:


print(feature_vectors)


# In[12]:


similarity=cosine_similarity(feature_vectors)


# In[13]:


print(similarity.shape)


# In[14]:


movie_name=input('Enter Your Fav movie name:')


# In[15]:


list_of_all_titles=movies_data['title'].tolist()
print(list_of_all_titles)


# In[16]:


find_close_match=difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)


# In[17]:


close_match=find_close_match[0]
print(close_match)


# In[18]:


index_of_the_movie=movies_data[movies_data.title==close_match]['index'].values[0]
print(index_of_the_movie)


# In[19]:


similarity_score=list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)


# In[20]:


len (similarity_score)


# In[21]:


sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1],reverse=True)
print(sorted_similar_movies)


# In[22]:


print('movies suggested for you: \n')
i=1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=movies_data[movies_data.index==index]['title'].values[0]
    if(i<10):
        print(i,'.',title_from_index)
        i+=1


# In[23]:


movie_name=input('Enter Your Fav movie name:')  
list_of_all_titles=movies_data['title'].tolist()
find_close_match=difflib.get_close_matches(movie_name, list_of_all_titles)
close_match=find_close_match[0]
index_of_the_movie=movies_data[movies_data.title==close_match]['index'].values[0]
similarity_score=list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1],reverse=True)
print('movies suggested for you: \n')
i=1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=movies_data[movies_data.index==index]['title'].values[0]
    if(i<10):
        print(i,'.',title_from_index)
        i+=1


# In[24]:


pip install colorama


# In[25]:


pip install ttkthemes


# ## Application Phase

# In[ ]:


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, Listbox, END
from colorama import Fore, Style

# Read the movies data from a CSV file
movies_data = pd.read_csv("movies.csv")

# Selecting features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Handling missing values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Creating combined features
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Cosine Similarity
similarity = cosine_similarity(feature_vectors)

# Define the recommendation function
def recommend_movies():
    movie_name = entry.get()
    find_close_match = difflib.get_close_matches(movie_name, movies_data['title'].tolist())
    
    # Clear the previous recommendations
    result_listbox.delete(0, END)

    if not find_close_match:
        result_listbox.insert(END, "Sorry, no close match found for the entered movie.")
        return

    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    result_listbox.insert(END, "Movies suggested for you:\n")
    for i, movie in enumerate(sorted_similar_movies[:10], start=1):
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        result_listbox.insert(END, f"{i}. {title_from_index}")

# Create the main GUI window
root = Tk()
root.title("Movie Recommendation System")

# Customize the appearance
root.configure(bg="black")
label = Label(root, text="Enter Your Favorite Movie:", bg="black", fg="skyblue", font=("Arial", 12))
entry = Entry(root, bg="black", fg="skyblue", font=("Arial", 12))
button = Button(root, text="Recommend Movies", command=recommend_movies, bg="blue", fg="white", font=("Arial", 12))
result_listbox = Listbox(root, width=50, height=10, selectbackground="yellow", selectmode="SINGLE", activestyle="none", bg="black", fg="skyblue", font=("Arial", 12))
scrollbar = Scrollbar(root, orient="vertical", command=result_listbox.yview, bg="black", troughcolor="blue")

result_listbox.config(yscrollcommand=scrollbar.set)

# Arrange GUI components
label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)
result_listbox.pack(pady=10)
scrollbar.pack(side="right", fill="y")

# Start the main loop
root.mainloop()



# In[ ]:





# In[ ]:




