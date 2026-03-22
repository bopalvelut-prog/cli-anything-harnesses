from setuptools import setup
setup(
    name='cli-anything-braco29',
    version='1.0.0',
    packages=['cli_anything.braco29'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco29=cli_anything.braco29:cli']},
)
