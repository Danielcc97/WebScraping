# WebScraping of Books to Scrape

Versión preliminar de la práctica 1 (Web scraping) de la asignatura Tipología y ciclo de vida de los datos del Máster en Ciencia de Datos en la Universitat Oberta de Catalunya. Se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web [Books to Scrape](https://books.toscrape.com) y generar un dataset.

### Instalación 🔧

_Para ejecutar el script es necesario instalar la siguientes bibliotecas:_

```
pip install BeautifulSoup
pip install os
pip install pandas
pip install random
pip install requests
pip install time
pip install tqdm
pip install urlparse
```

### Descripción de los ficheros 📋

* **jupyter/WebScraping.ipynb**: versión preliminar de la práctica realizada con Jupyter Notebook.
* **pyProject/main.py**: clase principal para el iniciar el scraping.
* **pyProject/scraper.py**: contiene la implementación de la clase _BooksScraper_ cuyos métodos extraen el conjunto de datos de la web [Books to Scrape](https://books.toscrape.com).
* **pyProject/book.py**: clase con las estructura de datos de un libro, y el método para convertir los datos a un formato CSV.
* **pyProject/output.png**: captura de pantalla de una ejecución del programa, con comentarios y tiempo que ha tardado.

## Despliegue-Ejecución 📦

_Accedemos a la ruta del proyecto pyProject, y ejecutamos la clase main:_
```
python main.py
```

## Build with 🛠️

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup) - A Python library designed for quick turnaround projects like screen-scraping.
* [Jupyter Notebook](https://jupyter.org) - An open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.
* [PyCharm](https://www.jetbrains.com/pycharm) - The Python IDE for Professional Developers.
* [Sourcetree](https://www.sourcetreeapp.com) - Simplicity and power in a beautiful Git GUI.

## Authors ✒️

* **Daniel Laureano Cerviño Cortínez** - *-* - [Danielcc97](https://github.com/Danielcc97)
* **Juan Kevin Trujillo Rodríguez** - *-* - [juankevinTR](https://juankevintrujillo.com)

## DOI 📖

El dataset ha sido subido a Zenodo y registrado con el DOI: [10.5281/zenodo.4263215](https://doi.org/10.5281/ZENODO.4263215)

## Referencias 🖇️

* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd.
* Subirats Maté, L., & Calvo González, M. (2019). Web scraping. Editorial UOC.
* Toscrape.com. (n.d.). Books to Scrape. Retrieved 7 November 2020, from https://books.toscrape.com/

## License 📄

Released Under CC0: Public Domain License



