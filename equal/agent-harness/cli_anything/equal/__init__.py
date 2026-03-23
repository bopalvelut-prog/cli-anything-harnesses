import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('equal running')
@cli.command()
def start(): click.echo('equal started')
if __name__ == '__main__': cli()
