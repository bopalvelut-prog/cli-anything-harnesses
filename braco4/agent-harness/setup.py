from setuptools import setup
setup(
    name='cli-anything-braco4',
    version='1.0.0',
    packages=['cli_anything.braco4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco4=cli_anything.braco4:cli']},
)
