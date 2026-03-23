from setuptools import setup
setup(
    name='cli-anything-chakra',
    version='1.0.0',
    packages=['cli_anything.chakra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chakra=cli_anything.chakra:cli']},
)
