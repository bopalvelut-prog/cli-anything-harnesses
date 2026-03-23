from setuptools import setup
setup(
    name='cli-anything-samba_v4',
    version='1.0.0',
    packages=['cli_anything.samba_v4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-samba_v4=cli_anything.samba_v4:cli']},
)
