from setuptools import setup
setup(
    name='cli-anything-patroni',
    version='1.0.0',
    packages=['cli_anything.patroni'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-patroni=cli_anything.patroni:cli']},
)
