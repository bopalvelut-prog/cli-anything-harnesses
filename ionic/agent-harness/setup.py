from setuptools import setup
setup(
    name='cli-anything-ionic',
    version='1.0.0',
    packages=['cli_anything.ionic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ionic=cli_anything.ionic:cli']},
)
