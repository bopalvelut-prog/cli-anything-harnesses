from setuptools import setup
setup(
    name='cli-anything-kibana',
    version='1.0.0',
    packages=['cli_anything.kibana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kibana=cli_anything.kibana:cli']},
)
