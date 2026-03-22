from setuptools import setup
setup(
    name='cli-anything-algorand',
    version='1.0.0',
    packages=['cli_anything.algorand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-algorand=cli_anything.algorand:cli']},
)
