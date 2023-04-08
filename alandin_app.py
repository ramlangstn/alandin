# library
import streamlit as st

# write
st.title('Ini tuh ceritanya Software Perkalian')
st.subheader('Masukin Angkanya')
st.write('jangan masukin huruf, apalagi duit')

#input bilangan pertama
number1 = st.number_input('masukan bilangan pertama')
st.write(f'bilangan pertama ialah {number1}')

#input bilangan pengali
number2 = st.number_input('masukan bilangan pengali')
st.write(f'bilangan pengali ialah {number2}')

#hasil kali
hasil= number1*number2

if st.button ('cek'):
    st.write(f'hasil kali antara keduanya adalah {hasil}')
else:
    st.write ('silahkan cek')



