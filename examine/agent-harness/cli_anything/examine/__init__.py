import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('examine running')
@cli.command()
def start(): click.echo('examine started')
if __name__ == '__main__': cli()
