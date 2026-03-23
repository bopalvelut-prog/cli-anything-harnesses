from setuptools import setup
setup(
    name='cli-anything-capacitor',
    version='1.0.0',
    packages=['cli_anything.capacitor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-capacitor=cli_anything.capacitor:cli']},
)
