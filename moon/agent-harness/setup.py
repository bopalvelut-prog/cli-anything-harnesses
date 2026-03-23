from setuptools import setup
setup(
    name='cli-anything-moon',
    version='1.0.0',
    packages=['cli_anything.moon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moon=cli_anything.moon:cli']},
)
