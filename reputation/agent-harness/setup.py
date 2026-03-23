from setuptools import setup
setup(
    name='cli-anything-reputation',
    version='1.0.0',
    packages=['cli_anything.reputation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reputation=cli_anything.reputation:cli']},
)
