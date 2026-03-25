# Dash-Bibliothek für die Web-App importieren
from dash import Dash, dcc, html

# Pandas für Datenverarbeitung
import pandas as pd

# NumPy für mathematische Berechnungen
import numpy as np

# Plotly Express für einfache Diagramme
import plotly.express as px

# Plotly Graph Objects für detaillierte Diagrammgestaltung
import plotly.graph_objects as go

# Plotly IO für das Speichern von Diagrammen
import plotly.io as pio

# Daten vorbereiten: Zwei Tabellen mit Beispielwerten erstellen
data1 = pd.DataFrame({'Spalte A': ['A1', 'A2', 'A3'], 'Wert': [10, 20, 30]})
data2 = pd.DataFrame({'Spalte B': ['B1', 'B2', 'B3'], 'Wert': [40, 50, 60]})

# Werte für die Normalverteilung erstellen: X-Werte von 50 bis 110 mit 100 Punkten
x_values = np.linspace(50, 110, 100)

# Normalverteilungsfunktion N(80,100) berechnen
y_values = (1 / np.sqrt(2 * np.pi * 100)) * np.exp(-((x_values - 80) ** 2) / (2 * 100))

# Dash-App initialisieren
app = Dash(__name__)

# Layout der Dash-App definieren
app.layout = html.Div([
    html.H1("Dashboard mit Grid"),  # Titel des Dashboards

    # Erste Zeile: Zwei Spalten für Tabellen
    html.Div([
        # Erste Spalte mit Tabelle 1
        html.Div([
            html.H3("Tabelle 1"),
            html.Table([
                # Tabellenkopf erstellen
                html.Tr([html.Th(col) for col in data1.columns])
            ] + [
                # Tabelleninhalt einfügen
                html.Tr([html.Td(data1.iloc[i][col]) for col in data1.columns]) for i in range(len(data1))
            ])
        ], style={'width': '50%', 'display': 'inline-block', 'backgroundColor': 'orange'}),

        # Zweite Spalte mit Tabelle 2
        html.Div([
            html.H3("Tabelle 2"),
            html.Table([
                html.Tr([html.Th(col) for col in data2.columns])  # Tabellenkopf
            ] + [
                html.Tr([html.Td(data2.iloc[i][col]) for col in data2.columns]) for i in range(len(data2))
            ])
        ], style={'width': '50%', 'display': 'inline-block'}),
    ]),

    # Zweite Zeile: Normalverteilungsplot in voller Breite
    html.Div([
        html.H3("Normalverteilungsplot N(80, 100)"),
        dcc.Graph(
            figure=px.line(x=x_values, y=y_values, title="Normalverteilung N(80,100)")
        )
    ], style={'width': '100%', 'marginTop': '20px'}),
])

# **2. Normalverteilungsplot speichern**
# Eine neue Plotly-Figur erstellen
fig = go.Figure()

# Normalverteilung als Linienplot hinzufügen
fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name="Normalverteilung N(80,100)"))

# Diagramm konfigurieren: Titel und Achsentitel setzen
fig.update_layout(title="Normalverteilung N(80,100)", xaxis_title="Werte", yaxis_title="Dichte")

# **Speicherung als JPG und PDF**
pio.write_image(fig, "normalverteilung.jpg")  # Speichert das Diagramm als JPG
pio.write_image(fig, "normalverteilung.pdf")  # Speichert das Diagramm als PDF

# Hauptfunktion: Startet die Dash-App
if __name__ == '__main__':
    app.run(debug=True)