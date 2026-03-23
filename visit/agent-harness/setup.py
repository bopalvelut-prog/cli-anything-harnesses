from setuptools import setup
setup(
    name='cli-anything-visit',
    version='1.0.0',
    packages=['cli_anything.visit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-visit=cli_anything.visit:cli']},
)
