from setuptools import setup
setup(
    name='cli-anything-liberal',
    version='1.0.0',
    packages=['cli_anything.liberal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-liberal=cli_anything.liberal:cli']},
)
