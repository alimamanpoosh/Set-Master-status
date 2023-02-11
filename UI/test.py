import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import requests
import pandas as pd
from pandas.io.json import json_normalize
import folium

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ########################################################
        header = {"Api-Key": "service.67a8012334664a739a502e74b84c0d65"}
        base_url = 'https://api.neshan.org'
        query = '/v1/search?term={SEARCH_TERM}&lat={LATITUDE}&lng={LONGITUDE}'
        url = base_url + query.format(
            SEARCH_TERM='دیدنی',
            LATITUDE='32.63680765',
            LONGITUDE='51.683308100000005'
        )
        print(url)
        r = requests.get(url, headers=header)
        r.ok
        historic = r.json()
        historic = json_normalize(historic['items'])
        historic.head(n=30)
        print(historic)
        print(type(historic))
        ####################################################
        #
        self.table = QtWidgets.QTableView()

        # data = pd.read_json(historic)
        #
        # data = [
        #   [4, 9, 2],
        #   [1, 0, 0],
        #   [3, 5, 0],
        #   [3, 3, 2],
        #   [7, 8, 9],
        # ]
        #
        self.model = TableModel(historic.values.tolist())
        self.table.setModel(self.model)
        #
        self.setCentralWidget(self.table)




app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
# app.exec
sys.exit(app.exec())