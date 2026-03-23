from setuptools import setup
setup(
    name='cli-anything-lightbend',
    version='1.0.0',
    packages=['cli_anything.lightbend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lightbend=cli_anything.lightbend:cli']},
)
