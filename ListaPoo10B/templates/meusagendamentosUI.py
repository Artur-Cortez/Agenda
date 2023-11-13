import streamlit as st
import pandas as pd
from views import View
import datetime
import time

class MeusAgendamentosUI:
  def main():
    MeusAgendamentosUI.listar()
    MeusAgendamentosUI.marcar()

  def listar():
    agendas = View.meus_agendamentos()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado no sistema")
    else:
      dic1 = []
      dic2 = []
      for obj in agendas:
        data = obj.get_data().strftime('%d/%m/%Y')
        hora = obj.get_data().strftime('%H:%M')
        servico = (View.servico_listar_id(obj.get_id_servico())).get_descricao()
        confirmado = obj.get_confirmado()
        if confirmado:
          dic1.append([data, hora, servico])
        else: dic2.append([data, hora, servico])
      df1 = pd.DataFrame(dic1, columns=["Data", "Hora", "Desc. do serviço"])
      df2 = pd.DataFrame(dic2, columns=["Data", "Hora", "Desc. do serviço"])
      st.header("Horários confirmados")
      if dic1 == []:
        st.write("Nenhum horário confirmado")
      else: st.dataframe(df1, hide_index=True)

      st.header("Horários a serem confirmados")
      if dic2 == []:
        st.write("Nenhum horário a ser confirmado")
      else: st.dataframe(df2, hide_index=True)
      
    
  def marcar():
    
    st.header("Reserve um horário para algo")
    horarios = View.agenda_listarsemana()
    opcao = st.selectbox("Selecione o horário", horarios, format_func= lambda x: f"{x.get_data().strftime('%d/%m/%Y')} - {View.semana[x.get_data().weekday()]} - {x.get_data().strftime('%H:%M')} ") 
    servicos = View.servico_listar()
    servico = st.selectbox("Selecione o serviço", servicos, format_func= lambda x: f"{x.get_descricao()} - R$ {x.get_valor():.2f} - {x.get_duracao()} min")
    if st.button("Inserir"):
      View.agenda_atualizar(opcao.get_id(), opcao.get_data(), False, st.session_state["cliente_id"], servico.get_id())
      st.success("Horário marcado com sucesso. Aguarde confirmação")
      time.sleep(0.5)
      st.rerun()