from setuptools import setup
setup(
    name='cli-anything-rigid',
    version='1.0.0',
    packages=['cli_anything.rigid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rigid=cli_anything.rigid:cli']},
)
