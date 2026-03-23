from setuptools import setup
setup(
    name='cli-anything-serious',
    version='1.0.0',
    packages=['cli_anything.serious'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-serious=cli_anything.serious:cli']},
)
