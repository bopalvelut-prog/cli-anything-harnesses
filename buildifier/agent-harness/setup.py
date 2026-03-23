from setuptools import setup
setup(
    name='cli-anything-buildifier',
    version='1.0.0',
    packages=['cli_anything.buildifier'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buildifier=cli_anything.buildifier:cli']},
)
