from setuptools import setup
setup(
    name='cli-anything-wallet',
    version='1.0.0',
    packages=['cli_anything.wallet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wallet=cli_anything.wallet:cli']},
)
