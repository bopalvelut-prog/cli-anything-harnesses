import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('capital running')
@cli.command()
def start(): click.echo('capital started')
if __name__ == '__main__': cli()
