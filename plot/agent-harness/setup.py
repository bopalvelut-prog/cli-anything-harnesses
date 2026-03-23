from setuptools import setup
setup(
    name='cli-anything-plot',
    version='1.0.0',
    packages=['cli_anything.plot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plot=cli_anything.plot:cli']},
)
