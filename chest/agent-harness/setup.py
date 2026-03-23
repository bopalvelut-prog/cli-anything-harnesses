from setuptools import setup
setup(
    name='cli-anything-chest',
    version='1.0.0',
    packages=['cli_anything.chest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chest=cli_anything.chest:cli']},
)
