from setuptools import setup
setup(
    name='cli-anything-trial',
    version='1.0.0',
    packages=['cli_anything.trial'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trial=cli_anything.trial:cli']},
)
