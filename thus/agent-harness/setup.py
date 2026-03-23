from setuptools import setup
setup(
    name='cli-anything-thus',
    version='1.0.0',
    packages=['cli_anything.thus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thus=cli_anything.thus:cli']},
)
