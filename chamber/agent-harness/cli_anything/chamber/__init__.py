import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chamber running')
@cli.command()
def start(): click.echo('chamber started')
if __name__ == '__main__': cli()
