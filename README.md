
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

### Opción 2: Archivo requirements.txt
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





## Explicación desarrollo 1 ejercicio

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




## Explicación desarrollo 2 ejercicio

Para el segundo ejercicio se desea desarrollar un microservicio para generar "Me Gusta" de las propiedades, a continuación se presenta el Diagrama Entidad Relación de la solución planteada.
| Indicador             | Descripción                                                                |
| ----------------- | ------------------------------------------------------------------ |
|![#D79B00](https://via.placeholder.com/10/D79B00?text=+)| Entidades iniciales.|
|![#82B366](https://via.placeholder.com/10/82B366?text=+) |Entidades propuestas. |

![2 Model](https://i.ibb.co/F05VHvB/Habi-DER.png)

En el diagrama anterior se presenta la solución generando una nueva entidad `interaction`, esta almacena el nombre (en este caso "Me Gusta") así como su correspondiente label.

Se genera la entidad `user`con los correspondientes parámetros (**NOTA: No se especifica dentro del modelo enviado por el evaluador, se creó un user simple con parámetros de acceso**).

Por último, se crea la estructura `interaction_history`, esta tabla almacena los registros de interacción entre usuarios y propiedad junto con el tipo de interacción que realizo, todo esto a partir de la fecha donde hizo la interacción.

### Queries de Creación

**user**
 ```SQL
/* Create Table */

CREATE TABLE `user` (
	`id` INT NOT NULL,
	`username` VARCHAR(20) NOT NULL,
	`password` VARCHAR(20) NOT NULL,
	CONSTRAINT `PK_USER` PRIMARY KEY (`id` ASC)
);
 ```

 
**interaction**
 ```SQL
/* Create Table */

CREATE TABLE `interaction` (
	`id` INT NOT NULL,
	`name` VARCHAR(32) NOT NULL,
	`label` VARCHAR(64) NULL,
	CONSTRAINT `PK_INTERACTION` PRIMARY KEY (`id` ASC)
);
 ```

 
**interaction_history**
 ```SQL
/* Create Table */

CREATE TABLE `interaction_history` (
	`id` INT NOT NULL,
	`interaction_id` INT NOT NULL,
	`property_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	`update_date` DATE NOT NULL,
	CONSTRAINT `PK_INTERACTION_HISTORY` PRIMARY KEY (`id` ASC)
);

/* Foreign Key Constraints */

ALTER TABLE `interaction_history` 
 ADD CONSTRAINT `FK_INTERACTION_INTERACTION_HISTORY`
	FOREIGN KEY (`interaction_id`) REFERENCES `interaction` (`id`) ON DELETE No Action ON UPDATE No Action;

ALTER TABLE `interaction_history` 
 ADD CONSTRAINT `FK_PROPERTY_INTERACTION_HISTORY`
	FOREIGN KEY (`property_id`) REFERENCES `property` (`id`) ON DELETE No Action ON UPDATE No Action;

ALTER TABLE `interaction_history` 
 ADD CONSTRAINT `FK_USER_INTERACTION_HISTORY`
	FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE No Action ON UPDATE No Action;
 ```

### Ventajas de la solución

Esta solución ofrece escalabilidad respecto a la posibilidad de nuevas interacciones ("No me gusta", "Favoritos", "Guardado" etc.), así mismo, es fácil agrupar las interacciones a partir de las funciones de agrupación SQL. Finalmente, se respetó el modelo base con nombres según la nomenclatura usada así como sintaxis y valores de datos según los datos ya presentes.
## Explicación desarrollo 3 ejercicio

En este ejercicio se pide ordenar un array separado por bloques, cada bloque se identifica por un 0, un bloque sin elementos se señala con una X.

Este proyecto se encuentra dentro de `src/list_organizer`, ejecutando el archivo `main.py`.

## Autor
Sergio Nicolás Ramírez Manrique
- nico98.snrm@gmail.com

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nico98snrm/)

