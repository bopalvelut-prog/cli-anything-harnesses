from setuptools import setup
setup(
    name='cli-anything-justify',
    version='1.0.0',
    packages=['cli_anything.justify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-justify=cli_anything.justify:cli']},
)
