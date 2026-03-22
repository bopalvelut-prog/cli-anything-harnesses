from setuptools import setup
setup(
    name='cli-anything-braco23',
    version='1.0.0',
    packages=['cli_anything.braco23'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco23=cli_anything.braco23:cli']},
)
