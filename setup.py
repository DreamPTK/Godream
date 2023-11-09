from setuptools import setup, find_packages

DESC ='This is a library that contain geospatial tools in python for Remote sensing and GIS applications. This project is part of Open data of Gistda project. ' 

setup(
    name='Godream',
    packages=['Godream'],
    version='0.0.1',
    license='MIT',
    author_email='dreamusaha@gmail.com',
    description= 'This is a library contained geospatial tools in python for jupyter environment ',
    long_description= DESC,
    author='Pathakorn Usaha',
    url= 'https://github.com/DreamPTK',
    download_url= 'https://pypi.org/project/Godream/',
    keywords= ['geography','geospatial','GIS', 'RS', 'Geospatial analysis'],
    install_requires= ["dask", "dask_ml", "xarray", 'joblib', 'datacube', 'rasterio', 'rioxarray', 'geopandas',' json', 'numpy', 'matplotlib', 'sklearn', 'os', 'logging', 'folium'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',      
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        ],
    )

