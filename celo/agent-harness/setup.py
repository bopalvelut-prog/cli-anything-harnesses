from setuptools import setup
setup(
    name='cli-anything-celo',
    version='1.0.0',
    packages=['cli_anything.celo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-celo=cli_anything.celo:cli']},
)
