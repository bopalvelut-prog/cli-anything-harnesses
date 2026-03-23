from setuptools import setup
setup(
    name='cli-anything-k3os',
    version='1.0.0',
    packages=['cli_anything.k3os'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-k3os=cli_anything.k3os:cli']},
)
