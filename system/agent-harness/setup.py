from setuptools import setup
setup(
    name='cli-anything-system',
    version='1.0.0',
    packages=['cli_anything.system'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-system=cli_anything.system:cli']},
)
