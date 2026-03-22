import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def devices(): subprocess.run(['adb', 'devices'])
@cli.command()
@click.argument('apk')
def install(apk): subprocess.run(['adb', 'install', apk])
@cli.command()
def shell(): subprocess.run(['adb', 'shell'])
@cli.command()
@click.argument('cmd')
def shell_cmd(cmd): subprocess.run(['adb', 'shell', cmd])
if __name__ == '__main__': cli()
