import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('introduce running')
@cli.command()
def start(): click.echo('introduce started')
if __name__ == '__main__': cli()
