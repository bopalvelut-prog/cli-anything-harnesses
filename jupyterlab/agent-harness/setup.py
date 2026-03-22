from setuptools import setup
setup(
    name='cli-anything-jupyterlab',
    version='1.0.0',
    packages=['cli_anything.jupyterlab'],
    install_requires=['nbformat'],
    entry_points={
        'console_scripts': [
            'cli-anything-jupyterlab=cli_anything.jupyterlab:cli',
        ],
    },
)
