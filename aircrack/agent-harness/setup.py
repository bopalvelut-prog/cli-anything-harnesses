from setuptools import setup
setup(
    name='cli-anything-aircrack',
    version='1.0.0',
    packages=['cli_anything.aircrack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aircrack=cli_anything.aircrack:cli']},
)
