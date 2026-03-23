from setuptools import setup
setup(
    name='cli-anything-cdi',
    version='1.0.0',
    packages=['cli_anything.cdi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cdi=cli_anything.cdi:cli']},
)
