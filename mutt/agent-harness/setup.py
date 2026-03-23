from setuptools import setup
setup(
    name='cli-anything-mutt',
    version='1.0.0',
    packages=['cli_anything.mutt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mutt=cli_anything.mutt:cli']},
)
