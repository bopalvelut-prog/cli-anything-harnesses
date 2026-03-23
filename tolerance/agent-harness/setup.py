from setuptools import setup
setup(
    name='cli-anything-tolerance',
    version='1.0.0',
    packages=['cli_anything.tolerance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tolerance=cli_anything.tolerance:cli']},
)
