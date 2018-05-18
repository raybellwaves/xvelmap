from setuptools import setup, find_packages

setup(name='cfanalytics',
      version='0.0.1',
      license='MIT',
      author='Benoit Bovy',      
      author_email='bbovy@gfz-potsdam.de',
      description='A xarray extension to show velocity fields as interactive maps in jupyterlab',
      url='https://github.com/benbovy/xvelmap',
      packages=find_packages(),
      install_requires=['json', 'xarray', 'ipython'],
      python_requires='>=3.6')
