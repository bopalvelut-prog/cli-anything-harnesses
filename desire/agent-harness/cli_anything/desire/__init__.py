import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('desire running')
@cli.command()
def start(): click.echo('desire started')
if __name__ == '__main__': cli()
