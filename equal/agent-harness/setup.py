from setuptools import setup
setup(
    name='cli-anything-equal',
    version='1.0.0',
    packages=['cli_anything.equal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-equal=cli_anything.equal:cli']},
)
