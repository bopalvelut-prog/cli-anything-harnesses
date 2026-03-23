import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smash running')
@cli.command()
def start(): click.echo('smash started')
if __name__ == '__main__': cli()
