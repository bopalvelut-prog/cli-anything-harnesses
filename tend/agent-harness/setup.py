from setuptools import setup
setup(
    name='cli-anything-tend',
    version='1.0.0',
    packages=['cli_anything.tend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tend=cli_anything.tend:cli']},
)
