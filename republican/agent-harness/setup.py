from setuptools import setup
setup(
    name='cli-anything-republican',
    version='1.0.0',
    packages=['cli_anything.republican'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-republican=cli_anything.republican:cli']},
)
