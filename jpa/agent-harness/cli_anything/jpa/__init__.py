import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jpa running')
@cli.command()
def start(): click.echo('jpa started')
if __name__ == '__main__': cli()
