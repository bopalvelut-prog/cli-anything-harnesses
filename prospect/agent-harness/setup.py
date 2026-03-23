from setuptools import setup
setup(
    name='cli-anything-prospect',
    version='1.0.0',
    packages=['cli_anything.prospect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prospect=cli_anything.prospect:cli']},
)
