import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('modern running')
@cli.command()
def start(): click.echo('modern started')
if __name__ == '__main__': cli()
