from setuptools import setup
setup(
    name='cli-anything-instana',
    version='1.0.0',
    packages=['cli_anything.instana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-instana=cli_anything.instana:cli']},
)
