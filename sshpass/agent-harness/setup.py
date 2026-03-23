from setuptools import setup
setup(
    name='cli-anything-sshpass',
    version='1.0.0',
    packages=['cli_anything.sshpass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sshpass=cli_anything.sshpass:cli']},
)
