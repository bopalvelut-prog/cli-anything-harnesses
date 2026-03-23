from setuptools import setup
setup(
    name='cli-anything-sandbox',
    version='1.0.0',
    packages=['cli_anything.sandbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sandbox=cli_anything.sandbox:cli']},
)
