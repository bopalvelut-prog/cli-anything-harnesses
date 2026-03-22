from setuptools import setup
setup(
    name='cli-anything-1inch',
    version='1.0.0',
    packages=['cli_anything.1inch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-1inch=cli_anything.1inch:cli']},
)
