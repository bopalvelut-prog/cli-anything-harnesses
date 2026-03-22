from setuptools import setup
setup(
    name='cli-anything-braco39',
    version='1.0.0',
    packages=['cli_anything.braco39'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco39=cli_anything.braco39:cli']},
)
