from setuptools import setup
setup(
    name='cli-anything-charge',
    version='1.0.0',
    packages=['cli_anything.charge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-charge=cli_anything.charge:cli']},
)
