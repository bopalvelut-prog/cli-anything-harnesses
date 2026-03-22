from setuptools import setup
setup(
    name='cli-anything-traefik',
    version='1.0.0',
    packages=['cli_anything.traefik'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-traefik=cli_anything.traefik:cli']},
)
