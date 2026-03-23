from setuptools import setup
setup(
    name='cli-anything-ansible_tower',
    version='1.0.0',
    packages=['cli_anything.ansible_tower'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ansible_tower=cli_anything.ansible_tower:cli']},
)
