from setuptools import setup
setup(
    name='cli-anything-verify',
    version='1.0.0',
    packages=['cli_anything.verify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-verify=cli_anything.verify:cli']},
)
