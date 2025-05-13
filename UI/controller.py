import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []
        self._coloreScelto = None
        self._annoScelto=None

    def fillDD(self):
        for i in range(2015,2019):
            self._view._ddyear.options.append(ft.dropdown.Option(f"{i}"))
        self._view.update_page()
        return


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        self._coloreScelto = self._view._ddcolor.value
        self._annoScelto =self._view._ddyear.value
        if self._coloreScelto is None or self._annoScelto is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("selezionare un colore e un anno"))
            self._view.update_page()
            return
        try:
            annoInt=int(self._annoScelto)
        except ValueError:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Errore"))
            self._view.update_page()
            return
        grafo=self._model.build_Graph(self._coloreScelto,annoInt)
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {grafo.number_of_nodes()} nodi e {grafo.number_of_edges()} archi"))
        massimi,nodiRipetuti=self._model.archiMax()
        for arco in massimi:
            self._view.txtOut.controls.append(ft.Text(arco))
        self._view.txtOut.controls.append(ft.Text(f"Nodi ripetuti: {nodiRipetuti}"))
        self._view.update_page()
        return





    def fillDDColor(self):
        colori = self._model._colori
        for colore in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(colore))
        self._view.update_page
        return


    def handle_search(self, e):
        pass
