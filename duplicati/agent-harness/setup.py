from setuptools import setup
setup(
    name='cli-anything-duplicati',
    version='1.0.0',
    packages=['cli_anything.duplicati'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-duplicati=cli_anything.duplicati:cli']},
)
