from setuptools import setup
setup(
    name='cli-anything-libyaml',
    version='1.0.0',
    packages=['cli_anything.libyaml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libyaml=cli_anything.libyaml:cli']},
)
