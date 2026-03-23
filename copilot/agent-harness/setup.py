from setuptools import setup
setup(
    name='cli-anything-copilot',
    version='1.0.0',
    packages=['cli_anything.copilot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-copilot=cli_anything.copilot:cli']},
)
