from IPython.display import Markdown, display
from dataclasses import dataclass

@dataclass
class A:
    Codigo_dpto: str = "Codigo_dpto"
    Departamento: str = "Departamento"
    Cod_municipio: str = "Cod_municipio"
    Municipio: str = "Municipio"    
    Latitud: str = "Latitud"    
    Longitud: str = "Longitud"
    Sexo: str = "Sexo"
    Fecha_beneficio_ó_Inicio: str = "Fecha beneficio ó Inicio"
    Clasificacion_Academica: str = "Clasificacion Academica"
    Entidad_Organización: str = "Entidad Organización"
    Programa: str = "Programa"
    Modalidad: str = "Modalidad"
    Beneficio: str = "Beneficio"



def salida(text):
    display(Markdown(text))

