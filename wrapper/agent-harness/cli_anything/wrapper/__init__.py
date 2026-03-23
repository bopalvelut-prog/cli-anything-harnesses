import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wrapper running')
@cli.command()
def start(): click.echo('wrapper started')
if __name__ == '__main__': cli()
