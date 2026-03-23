from setuptools import setup
setup(
    name='cli-anything-frame',
    version='1.0.0',
    packages=['cli_anything.frame'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-frame=cli_anything.frame:cli']},
)
