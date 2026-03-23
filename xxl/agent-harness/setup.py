from setuptools import setup
setup(
    name='cli-anything-xxl',
    version='1.0.0',
    packages=['cli_anything.xxl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xxl=cli_anything.xxl:cli']},
)
