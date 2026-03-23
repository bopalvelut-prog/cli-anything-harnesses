from setuptools import setup
setup(
    name='cli-anything-bracket',
    version='1.0.0',
    packages=['cli_anything.bracket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bracket=cli_anything.bracket:cli']},
)
