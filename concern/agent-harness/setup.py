from setuptools import setup
setup(
    name='cli-anything-concern',
    version='1.0.0',
    packages=['cli_anything.concern'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-concern=cli_anything.concern:cli']},
)
