from setuptools import setup
setup(
    name='cli-anything-conscious',
    version='1.0.0',
    packages=['cli_anything.conscious'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-conscious=cli_anything.conscious:cli']},
)
