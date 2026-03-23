import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guest running')
@cli.command()
def start(): click.echo('guest started')
if __name__ == '__main__': cli()
