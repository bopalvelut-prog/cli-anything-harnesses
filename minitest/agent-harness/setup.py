from setuptools import setup
setup(
    name='cli-anything-minitest',
    version='1.0.0',
    packages=['cli_anything.minitest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minitest=cli_anything.minitest:cli']},
)
