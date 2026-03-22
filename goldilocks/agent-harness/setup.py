from setuptools import setup
setup(
    name='cli-anything-goldilocks',
    version='1.0.0',
    packages=['cli_anything.goldilocks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-goldilocks=cli_anything.goldilocks:cli']},
)
