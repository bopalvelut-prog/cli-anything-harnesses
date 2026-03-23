import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('uuid running')
@cli.command()
def start(): click.echo('uuid started')
if __name__ == '__main__': cli()
