from setuptools import setup
setup(
    name='cli-anything-k6',
    version='1.0.0',
    packages=['cli_anything.k6'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-k6=cli_anything.k6:cli']},
)
