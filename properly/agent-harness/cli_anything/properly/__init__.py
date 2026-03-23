import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('properly running')
@cli.command()
def start(): click.echo('properly started')
if __name__ == '__main__': cli()
