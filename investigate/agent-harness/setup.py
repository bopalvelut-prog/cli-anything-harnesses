from setuptools import setup
setup(
    name='cli-anything-investigate',
    version='1.0.0',
    packages=['cli_anything.investigate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-investigate=cli_anything.investigate:cli']},
)
