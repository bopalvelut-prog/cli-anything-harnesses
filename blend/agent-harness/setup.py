from setuptools import setup
setup(
    name='cli-anything-blend',
    version='1.0.0',
    packages=['cli_anything.blend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blend=cli_anything.blend:cli']},
)
