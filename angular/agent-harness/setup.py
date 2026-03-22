from setuptools import setup
setup(
    name='cli-anything-angular',
    version='1.0.0',
    packages=['cli_anything.angular'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-angular=cli_anything.angular:cli']},
)
