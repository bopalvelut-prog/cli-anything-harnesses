from setuptools import setup
setup(
    name='cli-anything-combine',
    version='1.0.0',
    packages=['cli_anything.combine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-combine=cli_anything.combine:cli']},
)
