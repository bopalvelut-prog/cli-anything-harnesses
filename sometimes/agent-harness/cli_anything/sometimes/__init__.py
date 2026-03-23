import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sometimes running')
@cli.command()
def start(): click.echo('sometimes started')
if __name__ == '__main__': cli()
