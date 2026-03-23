from setuptools import setup
setup(
    name='cli-anything-congress',
    version='1.0.0',
    packages=['cli_anything.congress'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-congress=cli_anything.congress:cli']},
)
