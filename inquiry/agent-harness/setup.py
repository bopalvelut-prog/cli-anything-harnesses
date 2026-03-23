from setuptools import setup
setup(
    name='cli-anything-inquiry',
    version='1.0.0',
    packages=['cli_anything.inquiry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inquiry=cli_anything.inquiry:cli']},
)
