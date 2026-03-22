from setuptools import setup
setup(
    name='cli-anything-vsftpd',
    version='1.0.0',
    packages=['cli_anything.vsftpd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vsftpd=cli_anything.vsftpd:cli']},
)
