from setuptools import setup
setup(
    name='cli-anything-attack',
    version='1.0.0',
    packages=['cli_anything.attack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-attack=cli_anything.attack:cli']},
)
