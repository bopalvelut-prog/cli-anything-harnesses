from setuptools import setup
setup(
    name='cli-anything-figma',
    version='1.0.0',
    packages=['cli_anything.figma'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-figma=cli_anything.figma:cli']},
)
