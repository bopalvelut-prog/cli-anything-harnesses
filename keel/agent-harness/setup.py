from setuptools import setup
setup(
    name='cli-anything-keel',
    version='1.0.0',
    packages=['cli_anything.keel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keel=cli_anything.keel:cli']},
)
