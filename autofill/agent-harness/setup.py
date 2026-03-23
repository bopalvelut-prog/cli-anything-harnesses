from setuptools import setup
setup(
    name='cli-anything-autofill',
    version='1.0.0',
    packages=['cli_anything.autofill'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autofill=cli_anything.autofill:cli']},
)
