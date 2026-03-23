import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('relevant running')
@cli.command()
def start(): click.echo('relevant started')
if __name__ == '__main__': cli()
