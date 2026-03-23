from setuptools import setup
setup(
    name='cli-anything-pytest_xdist',
    version='1.0.0',
    packages=['cli_anything.pytest_xdist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pytest_xdist=cli_anything.pytest_xdist:cli']},
)
