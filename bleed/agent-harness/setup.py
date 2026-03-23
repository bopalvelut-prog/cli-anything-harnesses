from setuptools import setup
setup(
    name='cli-anything-bleed',
    version='1.0.0',
    packages=['cli_anything.bleed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bleed=cli_anything.bleed:cli']},
)
