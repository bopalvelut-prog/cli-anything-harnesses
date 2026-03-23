from setuptools import setup
setup(
    name='cli-anything-meld',
    version='1.0.0',
    packages=['cli_anything.meld'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meld=cli_anything.meld:cli']},
)
