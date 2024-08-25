import streamlit as st

st.title("The first streamlit app!")

st.header("_Streamlit_ is :green[FUN] :rocket: :star2: :hand:")
st.header("This is a header with a divider", divider="rainbow")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.markdown("* _Step 1_")
st.markdown("* _Step 2_")

st.header("Two", divider=True)
col1, col2 = st.columns(2)
with col1:
    x = st.slider("Choose and x value", 1,100)
with col2:
    st.write("the square of :red[**x**]is: ", x*x)

st.header("Three", divider=True)

st.header("Four", divider=True)
