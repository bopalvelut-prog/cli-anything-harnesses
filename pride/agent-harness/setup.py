from setuptools import setup
setup(
    name='cli-anything-pride',
    version='1.0.0',
    packages=['cli_anything.pride'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pride=cli_anything.pride:cli']},
)
