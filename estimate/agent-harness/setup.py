from setuptools import setup
setup(
    name='cli-anything-estimate',
    version='1.0.0',
    packages=['cli_anything.estimate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-estimate=cli_anything.estimate:cli']},
)
