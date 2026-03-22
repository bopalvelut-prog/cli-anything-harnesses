from setuptools import setup
setup(
    name='cli-anything-opencms',
    version='1.0.0',
    packages=['cli_anything.opencms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opencms=cli_anything.opencms:cli']},
)
