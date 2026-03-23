from setuptools import setup
setup(
    name='cli-anything-liquid',
    version='1.0.0',
    packages=['cli_anything.liquid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-liquid=cli_anything.liquid:cli']},
)
