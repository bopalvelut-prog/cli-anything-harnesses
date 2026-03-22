from setuptools import setup
setup(
    name='cli-anything-tailscale',
    version='1.0.0',
    packages=['cli_anything.tailscale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tailscale=cli_anything.tailscale:cli']},
)
