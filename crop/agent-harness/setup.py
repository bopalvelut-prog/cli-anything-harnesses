from setuptools import setup
setup(
    name='cli-anything-crop',
    version='1.0.0',
    packages=['cli_anything.crop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crop=cli_anything.crop:cli']},
)
