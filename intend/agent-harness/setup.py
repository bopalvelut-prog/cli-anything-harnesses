from setuptools import setup
setup(
    name='cli-anything-intend',
    version='1.0.0',
    packages=['cli_anything.intend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-intend=cli_anything.intend:cli']},
)
