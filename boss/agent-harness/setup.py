from setuptools import setup
setup(
    name='cli-anything-boss',
    version='1.0.0',
    packages=['cli_anything.boss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boss=cli_anything.boss:cli']},
)
