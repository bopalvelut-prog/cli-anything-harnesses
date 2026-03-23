from setuptools import setup
setup(
    name='cli-anything-grind',
    version='1.0.0',
    packages=['cli_anything.grind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grind=cli_anything.grind:cli']},
)
