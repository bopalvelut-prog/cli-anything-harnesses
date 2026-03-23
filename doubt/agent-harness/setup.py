from setuptools import setup
setup(
    name='cli-anything-doubt',
    version='1.0.0',
    packages=['cli_anything.doubt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-doubt=cli_anything.doubt:cli']},
)
