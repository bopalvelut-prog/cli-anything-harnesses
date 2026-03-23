from setuptools import setup
setup(
    name='cli-anything-vega',
    version='1.0.0',
    packages=['cli_anything.vega'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vega=cli_anything.vega:cli']},
)
