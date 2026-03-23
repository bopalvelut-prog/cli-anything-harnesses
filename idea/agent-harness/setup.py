from setuptools import setup
setup(
    name='cli-anything-idea',
    version='1.0.0',
    packages=['cli_anything.idea'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-idea=cli_anything.idea:cli']},
)
