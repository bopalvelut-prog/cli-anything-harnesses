from setuptools import setup
setup(
    name='cli-anything-sister',
    version='1.0.0',
    packages=['cli_anything.sister'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sister=cli_anything.sister:cli']},
)
