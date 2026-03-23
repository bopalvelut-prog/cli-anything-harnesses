from setuptools import setup
setup(
    name='cli-anything-pantheon',
    version='1.0.0',
    packages=['cli_anything.pantheon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pantheon=cli_anything.pantheon:cli']},
)
