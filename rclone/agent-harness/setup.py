from setuptools import setup
setup(
    name='cli-anything-rclone',
    version='1.0.0',
    packages=['cli_anything.rclone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rclone=cli_anything.rclone:cli']},
)
