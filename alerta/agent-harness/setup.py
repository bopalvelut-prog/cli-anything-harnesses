from setuptools import setup
setup(
    name='cli-anything-alerta',
    version='1.0.0',
    packages=['cli_anything.alerta'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alerta=cli_anything.alerta:cli']},
)
