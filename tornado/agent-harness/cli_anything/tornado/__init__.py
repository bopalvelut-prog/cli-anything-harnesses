import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tornado running')
@cli.command()
def start(): click.echo('tornado started')
if __name__ == '__main__': cli()
