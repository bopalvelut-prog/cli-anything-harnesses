from setuptools import setup
setup(
    name='cli-anything-necessarily',
    version='1.0.0',
    packages=['cli_anything.necessarily'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-necessarily=cli_anything.necessarily:cli']},
)
