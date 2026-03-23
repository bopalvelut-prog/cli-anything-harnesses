from setuptools import setup
setup(
    name='cli-anything-beacon',
    version='1.0.0',
    packages=['cli_anything.beacon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beacon=cli_anything.beacon:cli']},
)
