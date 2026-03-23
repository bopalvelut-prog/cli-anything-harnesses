from setuptools import setup
setup(
    name='cli-anything-freetds',
    version='1.0.0',
    packages=['cli_anything.freetds'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freetds=cli_anything.freetds:cli']},
)
