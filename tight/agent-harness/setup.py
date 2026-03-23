from setuptools import setup
setup(
    name='cli-anything-tight',
    version='1.0.0',
    packages=['cli_anything.tight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tight=cli_anything.tight:cli']},
)
