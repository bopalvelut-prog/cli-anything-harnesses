from setuptools import setup
setup(
    name='cli-anything-introduce',
    version='1.0.0',
    packages=['cli_anything.introduce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-introduce=cli_anything.introduce:cli']},
)
