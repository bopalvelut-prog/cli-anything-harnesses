from setuptools import setup
setup(
    name='cli-anything-reserve',
    version='1.0.0',
    packages=['cli_anything.reserve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reserve=cli_anything.reserve:cli']},
)
