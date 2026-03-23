import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prize running')
@cli.command()
def start(): click.echo('prize started')
if __name__ == '__main__': cli()
