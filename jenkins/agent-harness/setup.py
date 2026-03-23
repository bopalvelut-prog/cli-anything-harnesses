from setuptools import setup
setup(
    name='cli-anything-jenkins',
    version='1.0.0',
    packages=['cli_anything.jenkins'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jenkins=cli_anything.jenkins:cli']},
)
