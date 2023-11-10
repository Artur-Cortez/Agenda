import json
import datetime

class Agenda:
  def __init__(self, id, data, confirmado, nome_cliente, descricao_servico):
    self.__id = id
    self.__data = data
    self.__confirmado = confirmado
    self.__nome_cliente = nome_cliente
    self.__descricao_servico = descricao_servico

  def get_id(self): return self.__id
  def get_data(self): return self.__data
  def get_confirmado(self): return self.__confirmado
  def get_nome_cliente(self): return self.__nome_cliente
  def get_descricao_servico(self): return self.__descricao_servico

  def set_id(self, id): self.__id = id
  def set_data(self, data): self.__data = data
  def set_confirmado(self, confirmado): self.__confirmado = confirmado
  def set_nome_cliente(self, nome_cliente): self.__nome_cliente = nome_cliente
  def set_descricao_servico(self, descricao_servico): self.__descricao_servico = descricao_servico

  def __eq__(self, x):
    if self.__id == x.__id and self.__data == x.__data and self.__confirmado == x.__confirmado and self.__nome_cliente == x.__nome_cliente and self.__descricao_servico == x.__descricao_servico:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado} - {self.__nome_cliente} - {self.__descricao_servico}"

  def to_json(self):
    return {
      'id': self.__id,
      'data': self.__data.strftime('%d/%m/%Y %H:%M'),
      'confirmado': self.__confirmado,
      'nome_cliente': self.__nome_cliente,
      'descricao_servico': self.__descricao_servico}


class NAgenda:
  __agendas = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__agendas:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__agendas.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__agendas

  @classmethod
  def listar_nao_confirmados(cls):
    cls.abrir()
    nao_confirmados = []
    aux = datetime.datetime.now()
    hoje = datetime.datetime(aux.year, aux.month, aux.day)
    for aux in cls.__agendas:
      if not aux.__confirmado and aux.__data > hoje:
        nao_confirmados.append(aux)
    return nao_confirmados

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__agendas:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_data(obj.get_data())
      aux.set_confirmado(obj.get_confirmado())
      aux.set_nome_cliente(obj.get_nome_cliente())
      aux.set_descricao_servico(obj.get_descricao_servico())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__agendas.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__agendas = []
    try:
      with open("PEOOStreamlit/ListaPoo9D/models/agendas.json", mode="r") as arquivo:
        agendas_json = json.load(arquivo)
        for obj in agendas_json:
          aux = Agenda(
            obj["id"],
            datetime.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"),
            obj["confirmado"], obj["nome_cliente"], obj["descricao_servico"])
          cls.__agendas.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("PEOOStreamlit/ListaPoo9D/models/agendas.json", mode="w") as arquivo:
      json.dump(cls.__agendas, arquivo, default=Agenda.to_json)