from setuptools import setup
setup(
    name='cli-anything-suricata',
    version='1.0.0',
    packages=['cli_anything.suricata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suricata=cli_anything.suricata:cli']},
)
