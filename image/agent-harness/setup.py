from setuptools import setup
setup(
    name='cli-anything-image',
    version='1.0.0',
    packages=['cli_anything.image'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-image=cli_anything.image:cli']},
)
