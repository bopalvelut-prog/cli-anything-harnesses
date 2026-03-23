from setuptools import setup
setup(
    name='cli-anything-certain',
    version='1.0.0',
    packages=['cli_anything.certain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-certain=cli_anything.certain:cli']},
)
