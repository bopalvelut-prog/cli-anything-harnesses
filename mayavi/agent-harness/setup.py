from setuptools import setup
setup(
    name='cli-anything-mayavi',
    version='1.0.0',
    packages=['cli_anything.mayavi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mayavi=cli_anything.mayavi:cli']},
)
