from setuptools import setup
setup(
    name='cli-anything-offer',
    version='1.0.0',
    packages=['cli_anything.offer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-offer=cli_anything.offer:cli']},
)
