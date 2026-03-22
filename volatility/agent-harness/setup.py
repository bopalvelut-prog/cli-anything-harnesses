from setuptools import setup
setup(
    name='cli-anything-volatility',
    version='1.0.0',
    packages=['cli_anything.volatility'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-volatility=cli_anything.volatility:cli']},
)
