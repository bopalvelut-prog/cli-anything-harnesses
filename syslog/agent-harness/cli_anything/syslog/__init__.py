import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('syslog running')
@cli.command()
def start(): click.echo('syslog started')
if __name__ == '__main__': cli()
