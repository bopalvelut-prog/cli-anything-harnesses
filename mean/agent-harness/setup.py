from setuptools import setup
setup(
    name='cli-anything-mean',
    version='1.0.0',
    packages=['cli_anything.mean'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mean=cli_anything.mean:cli']},
)
