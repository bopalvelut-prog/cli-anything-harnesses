from setuptools import setup
setup(
    name='cli-anything-domestic',
    version='1.0.0',
    packages=['cli_anything.domestic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-domestic=cli_anything.domestic:cli']},
)
