from setuptools import setup
setup(
    name='cli-anything-linkedin',
    version='1.0.0',
    packages=['cli_anything.linkedin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linkedin=cli_anything.linkedin:cli']},
)
