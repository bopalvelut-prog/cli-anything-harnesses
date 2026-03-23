from setuptools import setup
setup(
    name='cli-anything-blame',
    version='1.0.0',
    packages=['cli_anything.blame'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blame=cli_anything.blame:cli']},
)
