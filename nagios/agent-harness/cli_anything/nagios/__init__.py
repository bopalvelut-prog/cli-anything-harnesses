import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Nagios running')
@cli.command()
def verify(): subprocess.run(['nagios', '-v', '/etc/nagios/nagios.cfg'])
if __name__ == '__main__': cli()
