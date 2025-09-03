import streamlit as st 
import seaborn as sns 
import plotly.express as px

st.title("explore Hidden Insights of Titanic Incident")

df = sns.load_dataset("titanic")
st.dataframe(df)

Gender = st.sidebar.multiselect('Gender', options = df['sex'].unique(), default = df['sex'].unique())
Pclass = st.sidebar.multiselect('Passenger Class', options = df['class'].unique(), default = df['class'].unique())

min_age, max_age = st.sidebar.slider('Age', min_value = int(df['age'].min()), max_value = int(df['age'].max()), value = (int(df['age'].min()), int(df['age'].max())))

filtered_df = df[
    (df['sex'].isin(Gender)) &
    (df['class'].isin(Pclass)) &
    (df['age']>=min_age )&
    (df['age']<=max_age)]

#Age Distribution
fig = px.histogram(df, x="age", nbins=30, title="Age Distribution")
st.plotly_chart(fig)

#Count of passenger class
fig = px.bar(df,x="class", title="Count of Passenger Class")
st.plotly_chart(fig)

#survival count based on gender
fig = px.bar(df, x="sex", color="survived", barmode="group", title="Survival Count Based on Gender")
st.plotly_chart(fig)