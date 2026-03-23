from setuptools import setup
setup(
    name='cli-anything-autodesk',
    version='1.0.0',
    packages=['cli_anything.autodesk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autodesk=cli_anything.autodesk:cli']},
)
