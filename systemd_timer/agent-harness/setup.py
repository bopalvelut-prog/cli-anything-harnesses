from setuptools import setup
setup(
    name='cli-anything-systemd_timer',
    version='1.0.0',
    packages=['cli_anything.systemd_timer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-systemd_timer=cli_anything.systemd_timer:cli']},
)
