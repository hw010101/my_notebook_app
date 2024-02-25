from setuptools import setup, find_packages

setup(
    name='my_notebook_app',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Gerekli bağımlılıkları buraya ekleyin
    ],
    entry_points={
        'console_scripts': [
            'my-notebook-app=my_notebook_app.main:main',
        ],
    },
)
