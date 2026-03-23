from setuptools import setup
setup(
    name='cli-anything-ultra',
    version='1.0.0',
    packages=['cli_anything.ultra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ultra=cli_anything.ultra:cli']},
)
