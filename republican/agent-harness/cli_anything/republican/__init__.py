import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('republican running')
@cli.command()
def start(): click.echo('republican started')
if __name__ == '__main__': cli()
