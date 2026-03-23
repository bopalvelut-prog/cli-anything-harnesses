from setuptools import setup
setup(
    name='cli-anything-dare',
    version='1.0.0',
    packages=['cli_anything.dare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dare=cli_anything.dare:cli']},
)
