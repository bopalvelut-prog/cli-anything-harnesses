from setuptools import setup
setup(
    name='cli-anything-terror',
    version='1.0.0',
    packages=['cli_anything.terror'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terror=cli_anything.terror:cli']},
)
