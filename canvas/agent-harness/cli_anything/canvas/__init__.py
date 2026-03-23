import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('canvas running')
@cli.command()
def start(): click.echo('canvas started')
if __name__ == '__main__': cli()
