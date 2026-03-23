import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('membership running')
@cli.command()
def start(): click.echo('membership started')
if __name__ == '__main__': cli()
