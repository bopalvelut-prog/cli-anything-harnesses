from setuptools import setup
setup(
    name='cli-anything-ascend',
    version='1.0.0',
    packages=['cli_anything.ascend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ascend=cli_anything.ascend:cli']},
)
