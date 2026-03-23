from setuptools import setup
setup(
    name='cli-anything-fear',
    version='1.0.0',
    packages=['cli_anything.fear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fear=cli_anything.fear:cli']},
)
