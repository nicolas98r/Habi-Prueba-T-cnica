
# Habi Prueba Técnica

Este repositorio es la solución de la prueba técnica para Desarrollador Ssr en la empresa Habi el día 07/03/2024. **[Link Enunciado](https://drive.google.com/file/d/1E1EJHjyzOWpqUZtsyuCNF96iBBsuNRGm/view?usp=sharing)**



## Tecnologías utilizadas

**Server:** Python 3.12.2, MySQL 


**Librerías:** 
- *mysql-connector-python:* Librería para conexión con MySQL.

- *python-dotenv:* Librería para manejo de archivos .env como variables de entorno.

- *jsonschema:* Librería para validación de parámetros de archivo JSON.

- *requests:* Librería para realizar peticiones HTTP.

## Instalación

Para la instalación del proyecto recuerde tener Python 3.12.2, puede instalar los requerimientos de 2 maneras;

### Opción 1: Poetry
Ejecute el comando de instalación de poetry.

```bash
  pip install poetry
```

Una vez instalado, ejecute el comando de instalación de dependencias con poetry.

```bash
  poetry install
```

Poetry facilita la instalación de dependencias al instalar las versiones recientes de las librerías así como la generación del entorno virtual para el proyecto.

### Opción 1: Archivo requirements.txt
Ejecute el comando de instalación de las dependencias mediante el archivo `requirements.txt`

```bash
  pip install -r requirements.txt
```
    
## Variables de Entorno

Para ejecutar este proyecto, debe añadir las siguientes variables de entorno a su archivo .env, estas variables son los datos de conexión a la Base de Datos MySQL

`DB_HOST`

`DB_PORT`

`DB_SCHEMA`

`DB_USER`

`DB_PASSWORD`

 **NOTA: Las credenciales de acceso fueron proporcionadas por el evaluador.**





## Explicación desarrollo 1ro ejercicio

Para el primer ejercicio sé pedía realizar un microservicio para obtener la lista de inmuebles vendidos como los disponibles. Dichos inmuebles pueden ser filtrados por varios valores. Por último los microservicios deben ser establecidos en arquitectura REST.

Para el ejercicio, se realizó el microservicio de búsqueda de propiedades en la carpeta `src/app` ejecutado el servidor mediante el archivo `main.py`.

El servicio genera un Handler que recibe una petición HTTP Post con la lista de filtros expresada de la siguiente manera:

#### Find Properties

```http
  POST /
```

**REQUEST BODY**

```JSON
  {
    "filters": [
        {
            "year": 2011
        },
        {
            "city": "bogota"
        },
        {
            "status": "pre_venta"
        }
    ]
}
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `filters` | `list` | **Required**. Lista de filtros. |
| `year` | `int` | Filtro por año. |
| `city` | `int` | Filtro por ciudad. |
| `status` | `int` | Filtro por estado. **Valores:** *pre_venta, en_venta, vendido*  |

**RESPONSE BODY**
```JSON
  [
    {
        "address": "Cll 1A #2B-3",
        "city": "bogota",
        "status": "pre_venta",
        "price": 300000000,
        "description": "Apartamento cerca al aeropuerto"
    },
    {
        "address": "Malabar Manzana B Casa 8",
        "city": "bogota",
        "status": "pre_venta",
        "price": 350000000,
        "description": "Casa campestre con hermosos paisajes"
    }
  ]
```

### Desarrollo

Para el desarrollo del servicio se genero un Handler HTTP que reconoce la petición post, este llama una función de validación del JSON según la estructura del Request Body (mediante JSONSchema), dicha estructura es enviada al Controller donde se añaden los filtros enviados formateando una query dentro de la BD. La query es ejecutada en la Base de Datos y luego esta es mapeada como una lista de Propiedades (JSON) que se retornan en el Response Body.




## Explicación desarrollo 2do ejercicio
## Explicación desarrollo 3er ejercicio


## Autor
Sergio Nicolás Ramírez Manrique
- nico98.snrm@gmail.com

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nico98snrm/)

