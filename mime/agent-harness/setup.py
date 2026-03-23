from setuptools import setup
setup(
    name='cli-anything-mime',
    version='1.0.0',
    packages=['cli_anything.mime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mime=cli_anything.mime:cli']},
)
