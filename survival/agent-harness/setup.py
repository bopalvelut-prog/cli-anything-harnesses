from setuptools import setup
setup(
    name='cli-anything-survival',
    version='1.0.0',
    packages=['cli_anything.survival'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-survival=cli_anything.survival:cli']},
)
