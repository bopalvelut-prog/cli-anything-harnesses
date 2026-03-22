from setuptools import setup
setup(
    name='cli-anything-ton',
    version='1.0.0',
    packages=['cli_anything.ton'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ton=cli_anything.ton:cli']},
)
