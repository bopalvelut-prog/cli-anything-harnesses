from setuptools import setup
setup(
    name='cli-anything-kraken',
    version='1.0.0',
    packages=['cli_anything.kraken'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kraken=cli_anything.kraken:cli']},
)
