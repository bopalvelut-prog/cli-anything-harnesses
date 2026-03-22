from setuptools import setup
setup(
    name='cli-anything-gphoto',
    version='1.0.0',
    packages=['cli_anything.gphoto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gphoto=cli_anything.gphoto:cli']},
)
