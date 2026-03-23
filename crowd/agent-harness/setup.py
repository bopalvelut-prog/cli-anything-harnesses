from setuptools import setup
setup(
    name='cli-anything-crowd',
    version='1.0.0',
    packages=['cli_anything.crowd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crowd=cli_anything.crowd:cli']},
)
