import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



def load_data():
    url = 'https://raw.githubusercontent.com/rfordatascience/' + \
    'tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv'
    df = pd.read_csv(url)
    df_interim = df.copy()
    df_interim = df_interim[['total_cup_points',
                                'species',
                                'country_of_origin',
                                'variety',
                                'aroma',
                                'aftertaste',
                                'acidity',
                                'body',
                                'balance',
                                'sweetness',
                                'altitude_mean_meters', 'moisture']]
    df_interim = df_interim.dropna()
    df_interim["species"] = pd.Categorical(df_interim["species"])
    df_interim["country_of_origin"] = pd.Categorical(df_interim["country_of_origin"])
    df_interim["variety"] = pd.Categorical(df_interim["variety"])
    df_interim["specialty"] = df_interim["total_cup_points"].apply(lambda x: "yes" if x>82.43 else "no")
    df_interim["specialty"] = pd.Categorical(df_interim["specialty"])
    df = df_interim.copy()
    return df
df_ch = load_data()
st.write(df_ch.shape[0])

st.title("Coffe dashboard")
st.dataframe(df_ch)
fig1 = px.histogram(df_ch, x="aroma")
st.plotly_chart(fig1)
fig2 = sns.pairplot(data = df_ch.select_dtypes("numbers"), hue="specialty")
st.pyplot(fig2.fig)
#x = st.slider("select value: ",min_value=-5,max_value=5, value = 0)
#st.write(x,"squared is",x**2)
#y = st.slider("select another value: ",min_value=-5,max_value=5, value = 0)
#st.write(x,"cubic is",y**3)
