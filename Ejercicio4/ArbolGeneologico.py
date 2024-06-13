import networkx as nx
import matplotlib.pyplot as plt

# Definimos la estructura de la familia
familia = {
    "abuelos": ["Luisa Chambi", "Atanacio Chambi"],
    "tios": ["Nicolasa Chambi Chambi", "Fidelia Chambi Chambi",],
    "padres": ["Raymundo Condori Cachaca", "Vicenta Chambi Chambi"],
    "hijos": ["Luis Alberto Condori Chambi", "Jose Luis Condori Chambi"],
    "primos": {
        "Fidelia Chambi Chambi": ["Fernando Isidro Chambi","Oscar Isidro Chambi", "Nancy Isidro Chambi", "Zulema Isidro Chambi", "Jayder Isidro Chambi", "Belinda Isidro Chambi"],
        "Nicolasa Chambi Chambi": ["Nelly Nina Chambi","Ramiro Nina Chambi", "Edwin Nina Chambi", "Raul Nina Chambi", "Maria Nina Chambi","Marco Nina Chambi"]
    }
}

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos y aristas para abuelos y padres
for abuelo in familia["abuelos"]:
    G.add_node(abuelo, level=0)
    
G.add_edge("Luisa Chambi", "Vicenta Chambi Chambi")
G.add_edge("Atanacio Chambi", "Vicenta Chambi Chambi")
G.add_edge("Luisa Chambi", "Nicolasa Chambi Chambi")
G.add_edge("Atanacio Chambi", "Nicolasa Chambi Chambi")
G.add_edge("Luisa Chambi", "Fidelia Chambi Chambi")
G.add_edge("Atanacio Chambi", "Fidelia Chambi Chambi")

# Añadir nodos y aristas para padres e hijos
G.add_edge("Vicenta Chambi Chambi", "Luis Alberto Condori Chambi")
G.add_edge("Raymundo Condori Cachaca", "Luis Alberto Condori Chambi")
G.add_edge("Vicenta Chambi Chambi", "Jose Luis Condori Chambi")
G.add_edge("Raymundo Condori Cachaca", "Jose Luis Condori Chambi")

# Añadir nodos y aristas para tios y primos
for primo, hijos in familia["primos"].items():
    for hijo in hijos:
        for tio in primo.split('_'):
            G.add_edge(tio, hijo)

# Definir las posiciones específicas de los nodos
pos = {
    "Luisa Chambi": (-2, 3),
    "Atanacio Chambi": (2, 3),
    
    "Fidelia Chambi Chambi": (4, 2.5),
    "Nicolasa Chambi Chambi": (0, 2.5),
    "Vicenta Chambi Chambi": (-4, 2.5),
    
    "Raymundo Condori Cachaca": (-8, 2.5),
    
    "Luis Alberto Condori Chambi": (-8, 2),
    "Jose Luis Condori Chambi": (-4, 2),
    
    "Fernando Isidro Chambi": (2, 1),
    "Oscar Isidro Chambi": (6, 1.5),
    "Nancy Isidro Chambi": (2, 1.5),
    "Zulema Isidro Chambi":(2, 2),
    "Jayder Isidro Chambi":(6, 2),
    "Belinda Isidro Chambi":(6, 1),
    
    "Nelly Nina Chambi":(-7,0.5),
    "Ramiro Nina Chambi":(-3,0.5),
    "Edwin Nina Chambi":(-1,1),
    "Raul Nina Chambi":(0, 0.5),
    "Maria Nina Chambi":(-5, 1.5),
    "Marco Nina Chambi":(-4,1),
    
    
}

plt.figure(figsize=(12, 8))
# Dibujar el grafo con posiciones específicas
nx.draw(G, pos, with_labels=True, node_size=4000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title("Árbol Genealógico de la Familia")
plt.show()
