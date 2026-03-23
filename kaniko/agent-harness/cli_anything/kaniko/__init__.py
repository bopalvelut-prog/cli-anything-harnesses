import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kaniko running')
@cli.command()
def start(): click.echo('kaniko started')
if __name__ == '__main__': cli()
