from setuptools import setup
setup(
    name='cli-anything-claim',
    version='1.0.0',
    packages=['cli_anything.claim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-claim=cli_anything.claim:cli']},
)
