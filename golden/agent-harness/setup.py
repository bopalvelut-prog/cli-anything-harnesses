from setuptools import setup
setup(
    name='cli-anything-golden',
    version='1.0.0',
    packages=['cli_anything.golden'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-golden=cli_anything.golden:cli']},
)
