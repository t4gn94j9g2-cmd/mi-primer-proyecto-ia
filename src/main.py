"""
Mi Primer Proyecto de Inteligencia Artificial
==============================================

Este es tu archivo principal. Aquí escribirás y ejecutarás tu código de IA.
"""

# Importar librerías básicas
import numpy as np
import pandas as pd

def bienvenida():
    """Función simple para empezar"""
    print("=" * 50)
    print("🤖 ¡Bienvenido a tu Primer Proyecto de IA! 🤖")
    print("=" * 50)
    print("\n✅ Las librerías están instaladas correctamente.")
    print("✅ Tu proyecto está listo para empezar.\n")

def ejemplo_numpy():
    """Ejemplo simple con NumPy"""
    print("📊 Ejemplo con NumPy:")
    print("-" * 50)
    
    # Crear un array (lista de números)
    numeros = np.array([1, 2, 3, 4, 5])
    print(f"Array: {numeros}")
    print(f"Suma: {numeros.sum()}")
    print(f"Promedio: {numeros.mean()}")
    print(f"Máximo: {numeros.max()}\n")

def ejemplo_pandas():
    """Ejemplo simple con Pandas"""
    print("📈 Ejemplo con Pandas:")
    print("-" * 50)
    
    # Crear un DataFrame (tabla de datos)
    datos = {
        'Nombre': ['Ana', 'Bob', 'Carlos'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
    }
    
    df = pd.DataFrame(datos)
    print(df)
    print(f"\nPromedio de edad: {df['Edad'].mean()}\n")

if __name__ == "__main__":
    bienvenida()
    ejemplo_numpy()
    ejemplo_pandas()
    print("✨ ¡Excelente! Ya tienes lo básico funcionando.")
