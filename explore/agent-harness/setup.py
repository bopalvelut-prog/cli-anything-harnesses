from setuptools import setup
setup(
    name='cli-anything-explore',
    version='1.0.0',
    packages=['cli_anything.explore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-explore=cli_anything.explore:cli']},
)
