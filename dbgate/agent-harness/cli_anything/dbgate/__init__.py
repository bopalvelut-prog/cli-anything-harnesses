import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dbgate running')
@cli.command()
def start(): click.echo('dbgate started')
if __name__ == '__main__': cli()
