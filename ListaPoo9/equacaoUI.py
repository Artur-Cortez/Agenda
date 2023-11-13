import streamlit as st
import pandas as pd
from ListaPoo9.equacao import Equacao

class EquacaoUI:
    def main():
        st.header("Equação do 2º Grau: a*x² + b*x + c")
        a = st.number_input("a")
        b = st.number_input("b")
        c = st.number_input("c")
        if st.button("Calcular"):
            eq = Equacao(a, b, c)
            st.write(eq)
            st.write(f"Delta = {eq.delta()}")
            if eq.TemRaizesReais():
                st.write(f"x1 = {eq.Raiz1()}")
                st.write(f"x2 = {eq.Raiz2()}")
                d = abs(eq.Raiz1()-eq.Raiz2())
                if d == 0: d = 4
                xmin = eq.Raiz2() - d/2
                xmax = eq.Raiz1() + d/2
            else:
                st.write("Não tem raízes reais")   
                xmin = -10
                xmax = 10 
            px = []
            py = []
            x = xmin
            while x < xmax * 1.005:
                px.append(x)
                py.append(eq.y(x))
                x += (xmax - xmin) / 50
            dic = { "x" : px, "y" : py }
            chart_data = pd.DataFrame(dic)
            st.line_chart(chart_data, x = "x", y = "y")    