from setuptools import setup
setup(
    name='cli-anything-village',
    version='1.0.0',
    packages=['cli_anything.village'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-village=cli_anything.village:cli']},
)
