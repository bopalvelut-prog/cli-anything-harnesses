from setuptools import setup
setup(
    name='cli-anything-sauce',
    version='1.0.0',
    packages=['cli_anything.sauce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sauce=cli_anything.sauce:cli']},
)
