from setuptools import setup
setup(
    name='cli-anything-v8',
    version='1.0.0',
    packages=['cli_anything.v8'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-v8=cli_anything.v8:cli']},
)
