from setuptools import setup
setup(
    name='cli-anything-bdd',
    version='1.0.0',
    packages=['cli_anything.bdd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bdd=cli_anything.bdd:cli']},
)
