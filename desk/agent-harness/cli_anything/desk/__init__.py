import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('desk running')
@cli.command()
def start(): click.echo('desk started')
if __name__ == '__main__': cli()
