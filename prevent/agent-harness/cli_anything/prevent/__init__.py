import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prevent running')
@cli.command()
def start(): click.echo('prevent started')
if __name__ == '__main__': cli()
