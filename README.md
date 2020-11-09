# Web Scraping of Books to Scrape

Versión definitiva de la práctica 1 (Web scraping) de la asignatura Tipología y ciclo de vida de los datos del Máster en Ciencia de Datos en la Universitat Oberta de Catalunya. Se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web [Books to Scrape](https://books.toscrape.com) y generar un dataset. La versión definitiva de esta práctica se trata de un proyecto escrito en Python, mientras que la versión preliminar con toda la lógica del proyecto es la que se encuentra en la carpeta jupyter.

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
* **pyProject/csv/dataset.csv**: dataset en CSV.
* **pyProject/html**: directorio dataset en HTML.

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

* Hong Khai, T. (2019, December 18). Extract Transform Load (ETL) for Books to Scrape. https://medium.com/analytics-vidhya/extract-transform-load-etl-for-books-to-scrape-b0ff5f83095d
* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd.
* Oheix, J. (2018, December 11). An introduction to web scraping with Python. https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-a2601e8619e5 
* Subirats Maté, L., & Calvo González, M. (2019). Web scraping. Editorial UOC.
* Toscrape.com. (n.d.). Books to Scrape. Retrieved 7 November 2020, from https://books.toscrape.com/

## License 📄

Released Under CC0: Public Domain License



