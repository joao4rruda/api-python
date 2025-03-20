import pyodbc

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.0.41;DATABASE=DW_TEXNEO_HOMOLOG;UID=ext.lizardti.01;PWD=rzQUB%YjT&pSg6')
        self.cursor = self.conn.cursor()

    def get_NotaFiscalEntradaItem(self):
        query = "SELECT * FROM [DW_TEXNEO_HOMOLOG].[lizard].[VW_EST_NotaFiscalEntradaItem]"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)

    def get_PedidosCompraItem(self):
        query = "SELECT * FROM [DW_TEXNEO_HOMOLOG].[lizard].[VW_SUP_PedidosCompraItem]"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)

    def get_SolicitacaoCompraItem(self):
        query = "SELECT * FROM [DW_TEXNEO_HOMOLOG].[lizard].[VW_SUP_SolicitacaoCompraItem]"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)

    def get_item(self, item_id):
        pass

    def add_item(self, id, body_object):
        pass

    def put_item(self, id, body_object):
        pass

    def delete_item(self, item_id):
        pass

db = ItemDatabase()
db.get_NotaFiscalEntradaItem()