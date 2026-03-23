from setuptools import setup
setup(
    name='cli-anything-whether',
    version='1.0.0',
    packages=['cli_anything.whether'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whether=cli_anything.whether:cli']},
)
