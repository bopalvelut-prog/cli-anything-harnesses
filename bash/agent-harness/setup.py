from setuptools import setup
setup(
    name='cli-anything-bash',
    version='1.0.0',
    packages=['cli_anything.bash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bash=cli_anything.bash:cli']},
)
