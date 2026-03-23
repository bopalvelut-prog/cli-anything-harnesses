import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('south running')
@cli.command()
def start(): click.echo('south started')
if __name__ == '__main__': cli()
