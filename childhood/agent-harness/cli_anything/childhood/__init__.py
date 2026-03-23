import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('childhood running')
@cli.command()
def start(): click.echo('childhood started')
if __name__ == '__main__': cli()
