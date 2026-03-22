from setuptools import setup
setup(
    name='cli-anything-mlflow',
    version='1.0.0',
    packages=['cli_anything.mlflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mlflow=cli_anything.mlflow:cli']},
)
