from setuptools import setup
setup(
    name='cli-anything-voter',
    version='1.0.0',
    packages=['cli_anything.voter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-voter=cli_anything.voter:cli']},
)
