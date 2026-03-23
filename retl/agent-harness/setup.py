from setuptools import setup
setup(
    name='cli-anything-retl',
    version='1.0.0',
    packages=['cli_anything.retl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retl=cli_anything.retl:cli']},
)
