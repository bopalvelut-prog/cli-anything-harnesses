from setuptools import setup
setup(
    name='cli-anything-neighbor',
    version='1.0.0',
    packages=['cli_anything.neighbor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-neighbor=cli_anything.neighbor:cli']},
)
