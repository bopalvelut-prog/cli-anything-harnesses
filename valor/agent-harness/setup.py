from setuptools import setup
setup(
    name='cli-anything-valor',
    version='1.0.0',
    packages=['cli_anything.valor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-valor=cli_anything.valor:cli']},
)
