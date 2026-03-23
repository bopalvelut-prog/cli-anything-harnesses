import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('uptime running')
@cli.command()
def start(): click.echo('uptime started')
if __name__ == '__main__': cli()
