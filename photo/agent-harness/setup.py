from setuptools import setup
setup(
    name='cli-anything-photo',
    version='1.0.0',
    packages=['cli_anything.photo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-photo=cli_anything.photo:cli']},
)
