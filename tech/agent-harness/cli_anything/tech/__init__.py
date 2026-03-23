import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tech running')
@cli.command()
def start(): click.echo('tech started')
if __name__ == '__main__': cli()
