import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slot running')
@cli.command()
def start(): click.echo('slot started')
if __name__ == '__main__': cli()
