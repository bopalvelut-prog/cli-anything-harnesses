from setuptools import setup
setup(
    name='cli-anything-ftx',
    version='1.0.0',
    packages=['cli_anything.ftx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ftx=cli_anything.ftx:cli']},
)
