from setuptools import setup
setup(
    name='cli-anything-grey',
    version='1.0.0',
    packages=['cli_anything.grey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grey=cli_anything.grey:cli']},
)
