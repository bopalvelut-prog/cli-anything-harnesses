from setuptools import setup
setup(
    name='cli-anything-cooperate',
    version='1.0.0',
    packages=['cli_anything.cooperate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cooperate=cli_anything.cooperate:cli']},
)
