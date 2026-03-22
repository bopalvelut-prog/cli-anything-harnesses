from setuptools import setup
setup(
    name='cli-anything-systemd',
    version='1.0.0',
    packages=['cli_anything.systemd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-systemd=cli_anything.systemd:cli']},
)
