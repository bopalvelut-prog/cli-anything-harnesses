from setuptools import setup
setup(
    name='cli-anything-boot',
    version='1.0.0',
    packages=['cli_anything.boot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boot=cli_anything.boot:cli']},
)
