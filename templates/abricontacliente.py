import streamlit as st
from views import View
import time

class AbrirContaCliente:
    def main():
        AbrirContaCliente.inserir()
        
    def inserir():
        aux = False
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        listar = View.cliente_listar()
        for i in listar:
            if i.get_email() == email:
                st.write("Email já existente. Favor trocar")
        
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha")
        if st.button("Inserir") and aux:
            View.cliente_inserir(nome, email, fone, senha)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()