from setuptools import setup
setup(
    name='cli-anything-xorg',
    version='1.0.0',
    packages=['cli_anything.xorg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xorg=cli_anything.xorg:cli']},
)
