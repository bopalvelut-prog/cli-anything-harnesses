from setuptools import setup
setup(
    name='cli-anything-ostree',
    version='1.0.0',
    packages=['cli_anything.ostree'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ostree=cli_anything.ostree:cli']},
)
