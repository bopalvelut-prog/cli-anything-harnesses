from setuptools import setup
setup(
    name='cli-anything-materialui',
    version='1.0.0',
    packages=['cli_anything.materialui'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-materialui=cli_anything.materialui:cli']},
)
