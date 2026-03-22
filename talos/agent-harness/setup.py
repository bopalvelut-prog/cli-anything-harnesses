from setuptools import setup
setup(
    name='cli-anything-talos',
    version='1.0.0',
    packages=['cli_anything.talos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-talos=cli_anything.talos:cli']},
)
