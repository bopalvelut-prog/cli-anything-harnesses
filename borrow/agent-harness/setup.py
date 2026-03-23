from setuptools import setup
setup(
    name='cli-anything-borrow',
    version='1.0.0',
    packages=['cli_anything.borrow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-borrow=cli_anything.borrow:cli']},
)
