import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('waste running')
@cli.command()
def start(): click.echo('waste started')
if __name__ == '__main__': cli()
