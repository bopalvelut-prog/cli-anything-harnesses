import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('avaya running')
@cli.command()
def start(): click.echo('avaya started')
if __name__ == '__main__': cli()
