from setuptools import setup
setup(
    name='cli-anything-rxpy',
    version='1.0.0',
    packages=['cli_anything.rxpy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rxpy=cli_anything.rxpy:cli']},
)
