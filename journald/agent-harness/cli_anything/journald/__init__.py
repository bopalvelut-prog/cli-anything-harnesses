import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def follow(): subprocess.run(['journalctl', '-f'])
@cli.command()
@click.argument('service')
def logs(service): subprocess.run(['journalctl', '-u', service])
@cli.command()
@click.argument('service')
def errors(service): subprocess.run(['journalctl', '-u', service, '-p', 'err'])
if __name__ == '__main__': cli()
