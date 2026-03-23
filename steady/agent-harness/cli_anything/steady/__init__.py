import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('steady running')
@cli.command()
def start(): click.echo('steady started')
if __name__ == '__main__': cli()
