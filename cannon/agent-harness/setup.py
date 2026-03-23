from setuptools import setup
setup(
    name='cli-anything-cannon',
    version='1.0.0',
    packages=['cli_anything.cannon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cannon=cli_anything.cannon:cli']},
)
