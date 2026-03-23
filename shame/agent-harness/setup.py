from setuptools import setup
setup(
    name='cli-anything-shame',
    version='1.0.0',
    packages=['cli_anything.shame'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shame=cli_anything.shame:cli']},
)
