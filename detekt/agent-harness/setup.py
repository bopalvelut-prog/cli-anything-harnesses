from setuptools import setup
setup(
    name='cli-anything-detekt',
    version='1.0.0',
    packages=['cli_anything.detekt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-detekt=cli_anything.detekt:cli']},
)
