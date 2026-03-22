from setuptools import setup
setup(
    name='cli-anything-braco25',
    version='1.0.0',
    packages=['cli_anything.braco25'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco25=cli_anything.braco25:cli']},
)
