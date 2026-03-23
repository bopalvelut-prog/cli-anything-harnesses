from setuptools import setup
setup(
    name='cli-anything-hetzner_storage',
    version='1.0.0',
    packages=['cli_anything.hetzner_storage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_storage=cli_anything.hetzner_storage:cli']},
)
