from setuptools import setup
setup(
    name='cli-anything-both',
    version='1.0.0',
    packages=['cli_anything.both'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-both=cli_anything.both:cli']},
)
