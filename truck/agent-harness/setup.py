from setuptools import setup
setup(
    name='cli-anything-truck',
    version='1.0.0',
    packages=['cli_anything.truck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-truck=cli_anything.truck:cli']},
)
