from setuptools import setup
setup(
    name='cli-anything-artery',
    version='1.0.0',
    packages=['cli_anything.artery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-artery=cli_anything.artery:cli']},
)
