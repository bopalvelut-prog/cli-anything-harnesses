import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yaml running')
@cli.command()
def start(): click.echo('yaml started')
if __name__ == '__main__': cli()
