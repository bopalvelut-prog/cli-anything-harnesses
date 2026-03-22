from setuptools import setup
setup(
    name='cli-anything-trustwallet',
    version='1.0.0',
    packages=['cli_anything.trustwallet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trustwallet=cli_anything.trustwallet:cli']},
)
