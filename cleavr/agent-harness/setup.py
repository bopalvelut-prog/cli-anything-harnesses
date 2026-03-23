from setuptools import setup
setup(
    name='cli-anything-cleavr',
    version='1.0.0',
    packages=['cli_anything.cleavr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cleavr=cli_anything.cleavr:cli']},
)
