from setuptools import setup
setup(
    name='cli-anything-ssh',
    version='1.0.0',
    packages=['cli_anything.ssh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ssh=cli_anything.ssh:cli']},
)
