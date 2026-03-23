from setuptools import setup
setup(
    name='cli-anything-hcloud',
    version='1.0.0',
    packages=['cli_anything.hcloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hcloud=cli_anything.hcloud:cli']},
)
