from setuptools import setup
setup(
    name='cli-anything-truth',
    version='1.0.0',
    packages=['cli_anything.truth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-truth=cli_anything.truth:cli']},
)
