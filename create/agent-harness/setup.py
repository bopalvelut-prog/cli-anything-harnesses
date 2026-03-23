from setuptools import setup
setup(
    name='cli-anything-create',
    version='1.0.0',
    packages=['cli_anything.create'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-create=cli_anything.create:cli']},
)
