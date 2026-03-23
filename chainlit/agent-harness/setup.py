from setuptools import setup
setup(
    name='cli-anything-chainlit',
    version='1.0.0',
    packages=['cli_anything.chainlit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chainlit=cli_anything.chainlit:cli']},
)
