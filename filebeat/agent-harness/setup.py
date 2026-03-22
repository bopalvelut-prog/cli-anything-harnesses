from setuptools import setup
setup(
    name='cli-anything-filebeat',
    version='1.0.0',
    packages=['cli_anything.filebeat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-filebeat=cli_anything.filebeat:cli']},
)
