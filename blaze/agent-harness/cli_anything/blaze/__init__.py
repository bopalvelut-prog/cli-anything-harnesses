import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blaze running')
@cli.command()
def start(): click.echo('blaze started')
if __name__ == '__main__': cli()
