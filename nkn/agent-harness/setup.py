from setuptools import setup
setup(
    name='cli-anything-nkn',
    version='1.0.0',
    packages=['cli_anything.nkn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nkn=cli_anything.nkn:cli']},
)
