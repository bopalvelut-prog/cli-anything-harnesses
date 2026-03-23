from setuptools import setup
setup(
    name='cli-anything-spike',
    version='1.0.0',
    packages=['cli_anything.spike'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spike=cli_anything.spike:cli']},
)
