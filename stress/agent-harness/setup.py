from setuptools import setup
setup(
    name='cli-anything-stress',
    version='1.0.0',
    packages=['cli_anything.stress'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stress=cli_anything.stress:cli']},
)
