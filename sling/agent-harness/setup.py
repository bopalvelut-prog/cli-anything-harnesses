from setuptools import setup
setup(
    name='cli-anything-sling',
    version='1.0.0',
    packages=['cli_anything.sling'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sling=cli_anything.sling:cli']},
)
