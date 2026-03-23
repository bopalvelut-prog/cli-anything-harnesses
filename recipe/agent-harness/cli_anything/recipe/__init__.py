import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recipe running')
@cli.command()
def start(): click.echo('recipe started')
if __name__ == '__main__': cli()
