# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    os.makedirs("docs", exist_ok=True)

    df = pd.read_csv("files/input/shipping-data.csv")

    # 1. envíos por almacén (barras verticales azules)
    counts = df["Warehouse_block"].value_counts().sort_index()
    plt.figure()
    counts.plot(kind="bar", color="#1f77b4")
    plt.title("Shipments per Warehouse")
    plt.xlabel("Warehouse block")
    plt.ylabel("Number of shipments")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # 2. modo de envío (donut chart)
    counts2 = df["Mode_of_Shipment"].value_counts().sort_index()
    plt.figure()
    wedges, texts, autotexts = plt.pie(
        counts2.values,
        labels=counts2.index,
        startangle=90,
        wedgeprops={"width": 0.4},
        autopct="%1.1f%%",
        colors=["#1f77b4", "#ff7f0e", "#2ca02c"]
    )
    plt.title("Mode of shipment")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # 3. calificación promedio cliente por modo de envío (barras horizontales naranjas)
    avg_rating = df.groupby("Mode_of_Shipment")["Customer_rating"].mean().sort_index()
    plt.figure()
    ax = avg_rating.plot(
        kind="barh",
        color="#ff7f0e"
    )
    ax.set_facecolor("#e0e0e0")
    plt.title("Average Customer Rating")
    plt.xlabel("Average rating")
    plt.ylabel("Mode of shipment")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

        # 4. distribución de peso (histograma naranjas)
    plt.figure()
    df["Weight_in_gms"].plot(
        kind="hist",
        bins=20,
        color="#ff7f0e"
    )
    plt.title("Shipped Weight Distribution")
    plt.xlabel("Weight in gms")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    # 5. crear index.html con layout 2x2
    html = '''
<html>
<head><title>Shipping Dashboard Example</title></head>
<body>
  <h1>Shipping Dashboard Example</h1>
  <table>
    <tr>
      <td><img src="shipping_per_warehouse.png" alt="Shipments per Warehouse" /></td>
      <td><img src="average_customer_rating.png" alt="Average Customer Rating" /></td>
    </tr>
    <tr>
      <td><img src="mode_of_shipment.png" alt="Mode of Shipment" /></td>
      <td><img src="weight_distribution.png" alt="Weight Distribution" /></td>
    </tr>
  </table>
</body>
</html>
'''
    with open("docs/index.html", "w") as f:
        f.write(html)