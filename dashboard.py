import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

file_path_p = "https://raw.githubusercontent.com/nndhiraa/proyek_analisis_data/main/data/cleaned_product_data.csv"
file_path_c = "https://raw.githubusercontent.com/nndhiraa/proyek_analisis_data/main/data/cleaned_customer_data.csv"
file_path_s = "https://raw.githubusercontent.com/nndhiraa/proyek_analisis_data/main/data/sellers_dataset.csv"
cleaned_data_c = pd.read_csv(file_path_c)
cleaned_data_p = pd.read_csv(file_path_p)
cleaned_data_s = pd.read_csv(file_path_s)


st.header('e-commerce stats 📈')

def disp_product_chart():
    category_top_count = cleaned_data_p['product_category'].value_counts().head(10)
    category_bottom_count = cleaned_data_p['product_category'].value_counts().tail(10)
    # Membuat dataframe
    top_category_df = pd.DataFrame({
        'Category': category_top_count.index,
        'Sales': category_top_count.values
    })

    # Membuat bar chart
    chart = alt.Chart(top_category_df).mark_bar().encode(
        x='Sales',
        y=alt.Y('Category', sort='-x'),  
        color=alt.value('#C1AAFF'),      
    ).properties(
        width=600,                         
        height=400,                        
        title='Best Selling Categories'
    )
    # Membuat dataframe
    bottom_category_df = pd.DataFrame({
        'Category': category_bottom_count.index,
        'Sales': category_bottom_count.values
    })
    # Membuat bar chart
    chart2 = alt.Chart(bottom_category_df).mark_bar().encode(
        x='Sales',
        y=alt.Y('Category', sort='-x'),  
        color=alt.value('#C1AAFF'),      
    ).properties(
        width=600,                         
        height=400,                         
        title='Worst Selling Categories'
    )

    # Menampilkan chart dengan st.altair_chart()
    st.altair_chart(chart, use_container_width=True) 
    st.altair_chart(chart2, use_container_width=True)   

def disp_customer_chart():
    top_state_count = cleaned_data_c['customer_state'].value_counts().head()
    top_city_count = cleaned_data_c['customer_city'].value_counts().head()
    # Membuat dataframe
    top_state_df = pd.DataFrame({
        'State': top_state_count.index,
        'Total': top_state_count.values
    })
    # Membuat bar chart
    chart = alt.Chart(top_state_df).mark_bar().encode(
        x='Total',
        y=alt.Y('State', sort='-x'),  
        color=alt.value('#9DFFAC'),      
    ).properties(
        width=600,                        
        height=400,                         
        title='State with the Most Customers'
    )
    # Membuat dataframe
    top_city_df = pd.DataFrame({
        'City': top_city_count.index,
        'Total': top_city_count.values
    })
    # Membuat bar chart
    chart2 = alt.Chart(top_city_df).mark_bar().encode(
        x='Total',
        y=alt.Y('City', sort='-x'),  
        color=alt.value('#9DFFAC'),      
    ).properties(
        width=600,                        
        height=400,                         
        title='City with the Most Customers'
    )

    # Menampilkan chart dengan st.altair_chart()
    st.altair_chart(chart, use_container_width=True)
    st.altair_chart(chart2, use_container_width=True)

def disp_seller_chart():
    top_state_count = cleaned_data_s['seller_state'].value_counts().head()
    top_city_count = cleaned_data_s['seller_city'].value_counts().head()
    # Membuat dataframe
    top_state_df = pd.DataFrame({
        'State': top_state_count.index,
        'Total': top_state_count.values
    })
    # Membuat bar chart
    chart = alt.Chart(top_state_df).mark_bar().encode(
        x='Total',
        y=alt.Y('State', sort='-x'),  
        color=alt.value('#89BBFF'),       
    ).properties(
        width=600,                        
        height=400,                         
        title='State with the Most Seller'
    )
    # Membuat dataframe
    top_city_df = pd.DataFrame({
        'City': top_city_count.index,
        'Total': top_city_count.values
    })
    # Membuat bar chart
    chart2 = alt.Chart(top_city_df).mark_bar().encode(
        x='Total',
        y=alt.Y('City', sort='-x'),  
        color=alt.value('#89BBFF'),       
    ).properties(
        width=600,                         
        height=400,                         
        title='City with the Most Seller'
    )

    # Menampilkan chart dengan st.altair_chart()
    st.altair_chart(chart, use_container_width=True)
    st.altair_chart(chart2, use_container_width=True)
 

st.sidebar.header('ecomm_')
product_button = st.sidebar.button("Product")
customer_button = st.sidebar.button("Customer")
seller_button = st.sidebar.button("Seller")
# Mendefinisikan isi tiap kategori
if product_button:
    st.subheader('Product Stats')
    st.write('Here are some information regarding products selling')
    disp_product_chart()
       
elif customer_button:
    st.subheader('Customer Stats')
    st.write('Here are some information regarding customer distribution by location')
    disp_customer_chart()
    st.write('Note: \n - Sao Paulo (SP)\n - Rio de Janeiro (RJ)\n - Minas Gerais (MG)\n - Rio Grande do Sul (RS)\n - Parana (PR)')

elif seller_button:
    st.subheader('Seller Stats')
    st.write('Here are some information regarding seller distribution by location')
    disp_seller_chart()
    st.write('Note: \n - Sao Paulo (SP)\n - Rio de Janeiro (RJ)\n - Minas Gerais (MG)\n - Santa Catarina (SC)\n - Parana (PR)')

st.write('Welcome to e-commerce stats, dashboard for e-commerce selling statistics. \n Here we have results of data analysis that can be accessed through sidebar: \n - Product \n - Customer \n - Seller')
