from setuptools import setup
setup(
    name='cli-anything-raydium',
    version='1.0.0',
    packages=['cli_anything.raydium'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-raydium=cli_anything.raydium:cli']},
)
