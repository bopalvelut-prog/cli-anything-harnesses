import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thermal running')
@cli.command()
def start(): click.echo('thermal started')
if __name__ == '__main__': cli()
