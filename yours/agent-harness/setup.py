from setuptools import setup
setup(
    name='cli-anything-yours',
    version='1.0.0',
    packages=['cli_anything.yours'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yours=cli_anything.yours:cli']},
)
