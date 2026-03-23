import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('private running')
@cli.command()
def start(): click.echo('private started')
if __name__ == '__main__': cli()
