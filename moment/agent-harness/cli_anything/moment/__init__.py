import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moment running')
@cli.command()
def start(): click.echo('moment started')
if __name__ == '__main__': cli()
