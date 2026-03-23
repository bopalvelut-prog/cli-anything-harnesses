from setuptools import setup
setup(
    name='cli-anything-pmd',
    version='1.0.0',
    packages=['cli_anything.pmd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pmd=cli_anything.pmd:cli']},
)
