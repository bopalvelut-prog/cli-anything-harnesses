from setuptools import setup
setup(
    name='cli-anything-testing',
    version='1.0.0',
    packages=['cli_anything.testing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-testing=cli_anything.testing:cli']},
)
