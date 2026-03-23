import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('avatar running')
@cli.command()
def start(): click.echo('avatar started')
if __name__ == '__main__': cli()
