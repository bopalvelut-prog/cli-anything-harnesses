from setuptools import setup
setup(
    name='cli-anything-bch',
    version='1.0.0',
    packages=['cli_anything.bch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bch=cli_anything.bch:cli']},
)
