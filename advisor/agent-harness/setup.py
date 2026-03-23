from setuptools import setup
setup(
    name='cli-anything-advisor',
    version='1.0.0',
    packages=['cli_anything.advisor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-advisor=cli_anything.advisor:cli']},
)
