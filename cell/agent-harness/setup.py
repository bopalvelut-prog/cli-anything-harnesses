from setuptools import setup
setup(
    name='cli-anything-cell',
    version='1.0.0',
    packages=['cli_anything.cell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cell=cli_anything.cell:cli']},
)
