from setuptools import setup
setup(
    name='cli-anything-conda',
    version='1.0.0',
    packages=['cli_anything.conda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-conda=cli_anything.conda:cli']},
)
