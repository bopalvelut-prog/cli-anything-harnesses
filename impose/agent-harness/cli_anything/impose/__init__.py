import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('impose running')
@cli.command()
def start(): click.echo('impose started')
if __name__ == '__main__': cli()
