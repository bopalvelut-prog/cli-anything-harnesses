from setuptools import setup
setup(
    name='cli-anything-incident',
    version='1.0.0',
    packages=['cli_anything.incident'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-incident=cli_anything.incident:cli']},
)
