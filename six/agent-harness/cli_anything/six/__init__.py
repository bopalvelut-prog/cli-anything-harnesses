import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('six running')
@cli.command()
def start(): click.echo('six started')
if __name__ == '__main__': cli()
