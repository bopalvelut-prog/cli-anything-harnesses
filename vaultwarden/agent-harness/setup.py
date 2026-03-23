from setuptools import setup
setup(
    name='cli-anything-vaultwarden',
    version='1.0.0',
    packages=['cli_anything.vaultwarden'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vaultwarden=cli_anything.vaultwarden:cli']},
)
