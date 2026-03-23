from setuptools import setup
setup(
    name='cli-anything-disorder',
    version='1.0.0',
    packages=['cli_anything.disorder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-disorder=cli_anything.disorder:cli']},
)
