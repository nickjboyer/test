
#### this is the line that works to run streamlit
#py -m streamlit run python_file.py

import streamlit as st
from random import randint


col1, col2, col3 = st.columns([1,2,1])


with col2:
    st.title("Dice Randomizer")
    num_dice = st.selectbox("Select the number of D6 dice to roll:", options=range(1, 6))

    
    button = st.button("Roll Dice")
    
    if button:
        results = [randint(1, 6) for _ in range(num_dice)]
        st.write(f"You rolled {num_dice} dice: ")
        result_str = ""
        result_num = 0
        for result in results:
            result_num += result
            result_str += str(result)+", "
        
        st.write(result_str[:-2])
        st.write(f"TOTAL = {result_num}")


