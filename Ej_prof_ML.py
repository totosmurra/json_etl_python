import json
import requests
import matplotlib.pyplot as plt

def fetch():
    with open ("mi_json_ML.json", "w") as jsonfile:
        response = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50")
        data = response.json()
        json.dump(data, jsonfile, indent = 4)
        datareal = data['results']

    
    deptos = [{"price":x["price"], "condition":x["condition"]} for x in datareal if x.get("currency_id") == "ARS"]
    deptosdumps = json.dumps(deptos, indent = 4)

    print(deptosdumps)

    return datareal




def transform(infofetch ,min, max):
    pricemin = len([{"price":x["price"]} for x in infofetch if x.get('price')<min])

    pricemid = len([{"price":x["price"]} for x in infofetch if min<x.get('price')<max])

    pricemax = len([{"price":x["price"]} for x in infofetch if max<x.get('price')])

    print(pricemin)
    print(pricemid)
    print(pricemax)

    preciosv = [pricemin, pricemid, pricemax]

    return preciosv
    


def report(preciosk, inforeportable):
    fig = plt.figure()
    fig.suptitle ("Precios de los Alquileres")

    ax = fig.add_subplot()

    ax.bar(preciosk ,inforeportable)
    ax.legend()
    plt.show()

if __name__ == '__main__':
    precio_maximo = 0
    precio_minimo = 0

    fetch()

    min = 6000
    max = 9000
    

    infofetch = fetch()
    
    inforeportable = transform(infofetch ,min, max)
    
    
    preciosk = ["Menos del valor minimo", "Entre ambos valores", "Mayor al valor maximo"]
    
    report(preciosk ,inforeportable)





    


