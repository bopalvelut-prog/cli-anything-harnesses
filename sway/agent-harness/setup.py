from setuptools import setup
setup(
    name='cli-anything-sway',
    version='1.0.0',
    packages=['cli_anything.sway'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sway=cli_anything.sway:cli']},
)
