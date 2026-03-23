from setuptools import setup
setup(
    name='cli-anything-stick',
    version='1.0.0',
    packages=['cli_anything.stick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stick=cli_anything.stick:cli']},
)
