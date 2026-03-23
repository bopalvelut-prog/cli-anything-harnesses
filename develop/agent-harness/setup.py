from setuptools import setup
setup(
    name='cli-anything-develop',
    version='1.0.0',
    packages=['cli_anything.develop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-develop=cli_anything.develop:cli']},
)
