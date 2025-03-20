import pyodbc

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.0.41;DATABASE=DW_TEXNEO_HOMOLOG;UID=ext.lizardti.01;PWD=rzQUB%YjT&pSg6')
        self.cursor = self.conn.cursor()

    def get_NotaFiscalEntradaItem(self):
        result = []
        query = "SELECT * FROM [DW_TEXNEO_HOMOLOG].[lizard].[VW_EST_NotaFiscalEntradaItem]"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            nota_fiscal_entrada_item_dict = {}
            nota_fiscal_entrada_item_dict["ID"] = row[0]
            nota_fiscal_entrada_item_dict["NEI_EmpresaCod"] = row[1]
            nota_fiscal_entrada_item_dict["NEI_PedidoItemCod"] = row[2]
            result.append(nota_fiscal_entrada_item_dict)

        print(result)

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