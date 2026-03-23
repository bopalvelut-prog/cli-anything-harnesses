from setuptools import setup
setup(
    name='cli-anything-often',
    version='1.0.0',
    packages=['cli_anything.often'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-often=cli_anything.often:cli']},
)
