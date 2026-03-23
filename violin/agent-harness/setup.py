from setuptools import setup
setup(
    name='cli-anything-violin',
    version='1.0.0',
    packages=['cli_anything.violin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-violin=cli_anything.violin:cli']},
)
