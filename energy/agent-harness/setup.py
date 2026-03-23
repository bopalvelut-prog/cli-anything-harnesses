from setuptools import setup
setup(
    name='cli-anything-energy',
    version='1.0.0',
    packages=['cli_anything.energy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-energy=cli_anything.energy:cli']},
)
