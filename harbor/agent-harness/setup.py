from setuptools import setup
setup(
    name='cli-anything-harbor',
    version='1.0.0',
    packages=['cli_anything.harbor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-harbor=cli_anything.harbor:cli']},
)
