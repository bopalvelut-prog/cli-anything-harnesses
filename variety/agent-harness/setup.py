from setuptools import setup
setup(
    name='cli-anything-variety',
    version='1.0.0',
    packages=['cli_anything.variety'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-variety=cli_anything.variety:cli']},
)
