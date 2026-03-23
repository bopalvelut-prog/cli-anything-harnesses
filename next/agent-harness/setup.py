from setuptools import setup
setup(
    name='cli-anything-next',
    version='1.0.0',
    packages=['cli_anything.next'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-next=cli_anything.next:cli']},
)
