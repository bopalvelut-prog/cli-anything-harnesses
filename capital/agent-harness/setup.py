from setuptools import setup
setup(
    name='cli-anything-capital',
    version='1.0.0',
    packages=['cli_anything.capital'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-capital=cli_anything.capital:cli']},
)
