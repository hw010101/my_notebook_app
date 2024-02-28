from setuptools import setup, find_packages

setup(
    name='my_notebook_app',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'yavuz_unique==0.1.6',  # Gerekli bağımlılıkları buraya ekleyin
    ],
    entry_points={
        'console_scripts': [
            'my-notebook-app=my_notebook_app.main:main',
        ],
    },
    author='lilzey',
    author_email='lilzey0101@gmail.com',
    description='notebook',
    url='https://github.com/hw010101/my_notebook_app',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
        'Source': 'https://github.com/hw010101/my_notebook_app',
    },
)
