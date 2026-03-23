from setuptools import setup
setup(
    name='cli-anything-negotiate',
    version='1.0.0',
    packages=['cli_anything.negotiate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-negotiate=cli_anything.negotiate:cli']},
)
