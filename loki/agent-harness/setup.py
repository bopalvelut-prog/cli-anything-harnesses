from setuptools import setup
setup(
    name='cli-anything-loki',
    version='1.0.0',
    packages=['cli_anything.loki'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-loki=cli_anything.loki:cli']},
)
