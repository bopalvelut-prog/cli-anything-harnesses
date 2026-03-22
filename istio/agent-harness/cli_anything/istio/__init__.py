import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['istioctl', 'install'])
@cli.command()
def status(): subprocess.run(['istioctl', 'analyze'])
@cli.command()
def proxy(): subprocess.run(['istioctl', 'proxy-status'])
if __name__ == '__main__': cli()
