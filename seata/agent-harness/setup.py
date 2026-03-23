from setuptools import setup
setup(
    name='cli-anything-seata',
    version='1.0.0',
    packages=['cli_anything.seata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seata=cli_anything.seata:cli']},
)
