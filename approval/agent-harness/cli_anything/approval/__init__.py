import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('approval running')
@cli.command()
def start(): click.echo('approval started')
if __name__ == '__main__': cli()
