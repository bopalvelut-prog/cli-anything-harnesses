from setuptools import setup
setup(
    name='cli-anything-van',
    version='1.0.0',
    packages=['cli_anything.van'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-van=cli_anything.van:cli']},
)
