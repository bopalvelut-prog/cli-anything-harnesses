from setuptools import setup
setup(
    name='cli-anything-tendency',
    version='1.0.0',
    packages=['cli_anything.tendency'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tendency=cli_anything.tendency:cli']},
)
