from setuptools import setup
setup(
    name='cli-anything-sufficient',
    version='1.0.0',
    packages=['cli_anything.sufficient'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sufficient=cli_anything.sufficient:cli']},
)
