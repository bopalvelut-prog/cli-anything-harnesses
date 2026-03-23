from setuptools import setup
setup(
    name='cli-anything-ridge',
    version='1.0.0',
    packages=['cli_anything.ridge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ridge=cli_anything.ridge:cli']},
)
