from setuptools import setup
setup(
    name='cli-anything-honey',
    version='1.0.0',
    packages=['cli_anything.honey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-honey=cli_anything.honey:cli']},
)
