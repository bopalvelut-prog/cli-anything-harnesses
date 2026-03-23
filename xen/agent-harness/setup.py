from setuptools import setup
setup(
    name='cli-anything-xen',
    version='1.0.0',
    packages=['cli_anything.xen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xen=cli_anything.xen:cli']},
)
