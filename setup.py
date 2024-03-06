from setuptools import setup, find_packages

setup(
    name='my_notebook_app',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'yavuz-unique==0.1.7',
        'my-notebook-app==0.1.4',
        'lilzey==0.1.1',
        'zenith-tea==0.1.0',
        'zoraapexx==0.1.0',
        'requests==2.26.0',
        'cann_calculator==1.0.0',
        'flask==2.1.1',
     ],
    entry_points={
        'console_scripts': [
            'my-notebook-app=my_notebook_app.main:main',
        ],
    },
    author='lilzey',
    author_email='lilzey0101@gmail.com',
    description='notebook',
    bugtrack_url='https://github.com/hw010101/my_notebook_app',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
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
