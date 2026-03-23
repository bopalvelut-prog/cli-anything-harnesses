from setuptools import setup
setup(
    name='cli-anything-jazz',
    version='1.0.0',
    packages=['cli_anything.jazz'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jazz=cli_anything.jazz:cli']},
)
