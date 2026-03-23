from setuptools import setup
setup(
    name='cli-anything-retain',
    version='1.0.0',
    packages=['cli_anything.retain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retain=cli_anything.retain:cli']},
)
