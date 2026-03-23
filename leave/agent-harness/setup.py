from setuptools import setup
setup(
    name='cli-anything-leave',
    version='1.0.0',
    packages=['cli_anything.leave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leave=cli_anything.leave:cli']},
)
