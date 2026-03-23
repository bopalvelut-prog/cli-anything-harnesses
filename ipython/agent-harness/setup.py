from setuptools import setup
setup(
    name='cli-anything-ipython',
    version='1.0.0',
    packages=['cli_anything.ipython'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ipython=cli_anything.ipython:cli']},
)
