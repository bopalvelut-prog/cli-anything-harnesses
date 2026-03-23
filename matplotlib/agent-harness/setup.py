from setuptools import setup
setup(
    name='cli-anything-matplotlib',
    version='1.0.0',
    packages=['cli_anything.matplotlib'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-matplotlib=cli_anything.matplotlib:cli']},
)
