import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('host running')
@cli.command()
def start(): click.echo('host started')
if __name__ == '__main__': cli()
