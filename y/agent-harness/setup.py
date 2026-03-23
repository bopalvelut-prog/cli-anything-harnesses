from setuptools import setup
setup(
    name='cli-anything-y',
    version='1.0.0',
    packages=['cli_anything.y'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-y=cli_anything.y:cli']},
)
