from setuptools import setup
setup(
    name='cli-anything-dawn',
    version='1.0.0',
    packages=['cli_anything.dawn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dawn=cli_anything.dawn:cli']},
)
