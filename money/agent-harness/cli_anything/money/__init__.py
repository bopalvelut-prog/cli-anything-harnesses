import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('money running')
@cli.command()
def start(): click.echo('money started')
if __name__ == '__main__': cli()
