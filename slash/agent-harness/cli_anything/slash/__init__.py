import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slash running')
@cli.command()
def start(): click.echo('slash started')
if __name__ == '__main__': cli()
