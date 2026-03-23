from setuptools import setup
setup(
    name='cli-anything-inflation',
    version='1.0.0',
    packages=['cli_anything.inflation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inflation=cli_anything.inflation:cli']},
)
