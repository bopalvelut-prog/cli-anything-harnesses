from setuptools import setup
setup(
    name='cli-anything-circle',
    version='1.0.0',
    packages=['cli_anything.circle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-circle=cli_anything.circle:cli']},
)
