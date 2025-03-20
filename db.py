import pyodbc

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=172.16.0.41;DATABASE=DW_TEXNEO_HOMOLOG;UID=ext.lizardti.01;PWD=rzQUB%YjT&pSg6')  # Insira sua string de conexão
        self.cursor = self.conn.cursor()

    def get_NotaFiscalEntradaItem(self):
        result = []
        query = "SELECT * FROM [DW_TEXNEO_HOMOLOG].[lizard].[VW_EST_NotaFiscalEntradaItem]"
        self.cursor.execute(query)
        columns = [column[0] for column in self.cursor.description]  # Obtém os nomes das colunas

        for row in self.cursor.fetchall():
            result.append(dict(zip(columns, row)))  # Mapeia colunas para valores

        return result

    def get_PedidosCompraItem(self):
        result = []
        query = "SELECT * FROM [DW_TEXNEO_HOMOLOG].[lizard].[VW_SUP_PedidosCompraItem]"
        self.cursor.execute(query)
        columns = [column[0] for column in self.cursor.description]  # Obtém os nomes das colunas

        for row in self.cursor.fetchall():
            result.append(dict(zip(columns, row)))  # Mapeia colunas para valores

        return result

    def get_SolicitacaoCompraItem(self):
        result = []
        query = "SELECT * FROM [DW_TEXNEO_HOMOLOG].[lizard].[VW_SUP_SolicitacaoCompraItem]"
        self.cursor.execute(query)
        columns = [column[0] for column in self.cursor.description]  # Obtém os nomes das colunas

        for row in self.cursor.fetchall():
            result.append(dict(zip(columns, row)))

        return result

db = ItemDatabase()
