from setuptools import setup
setup(
    name='cli-anything-wage',
    version='1.0.0',
    packages=['cli_anything.wage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wage=cli_anything.wage:cli']},
)
