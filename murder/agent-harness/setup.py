from setuptools import setup
setup(
    name='cli-anything-murder',
    version='1.0.0',
    packages=['cli_anything.murder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-murder=cli_anything.murder:cli']},
)
