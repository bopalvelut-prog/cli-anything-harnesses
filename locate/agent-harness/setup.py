from setuptools import setup
setup(
    name='cli-anything-locate',
    version='1.0.0',
    packages=['cli_anything.locate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-locate=cli_anything.locate:cli']},
)
