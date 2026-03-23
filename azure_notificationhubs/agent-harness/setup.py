from setuptools import setup
setup(
    name='cli-anything-azure_notificationhubs',
    version='1.0.0',
    packages=['cli_anything.azure_notificationhubs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_notificationhubs=cli_anything.azure_notificationhubs:cli']},
)
