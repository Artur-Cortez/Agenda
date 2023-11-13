from ListaPoo9b.cliente import Cliente, NCliente

class View:
    @classmethod
    def cliente_inserir(cls, nome, email, fone):
        c = Cliente(0, nome, email, fone)
        NCliente.inserir(c)
    
    @classmethod
    def cliente_listar(cls):
        return NCliente.listar()
    
    @classmethod
    def cliente_atualizar(cls, id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        NCliente.atualizar(c)
    
    @classmethod
    def cliente_excluir(cls, id):
        c = NCliente.listar_id(id)
        NCliente.excluir(c)