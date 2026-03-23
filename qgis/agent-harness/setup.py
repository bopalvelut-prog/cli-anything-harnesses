from setuptools import setup
setup(
    name='cli-anything-qgis',
    version='1.0.0',
    packages=['cli_anything.qgis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qgis=cli_anything.qgis:cli']},
)
