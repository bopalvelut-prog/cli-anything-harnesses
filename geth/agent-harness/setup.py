from setuptools import setup
setup(
    name='cli-anything-geth',
    version='1.0.0',
    packages=['cli_anything.geth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-geth=cli_anything.geth:cli']},
)
