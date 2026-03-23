from setuptools import setup
setup(
    name='cli-anything-okhttp',
    version='1.0.0',
    packages=['cli_anything.okhttp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-okhttp=cli_anything.okhttp:cli']},
)
