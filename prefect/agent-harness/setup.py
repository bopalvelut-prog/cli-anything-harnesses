from setuptools import setup
setup(
    name='cli-anything-prefect',
    version='1.0.0',
    packages=['cli_anything.prefect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prefect=cli_anything.prefect:cli']},
)
