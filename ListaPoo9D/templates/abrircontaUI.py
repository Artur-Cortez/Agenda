import streamlit as st
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      clientes = View.cliente_listar()
      for i in clientes:
        if i.get_email() == email:
          st.error("Já existe outro cliente com esse mesmo e-mail")
      else:
        View.cliente_inserir(nome, email, fone, senha)
        st.success("Cliente inserido com sucesso")
        time.sleep(2)
        st.rerun()
