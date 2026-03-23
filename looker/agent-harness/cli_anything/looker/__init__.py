import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('looker running')
@cli.command()
def start(): click.echo('looker started')
if __name__ == '__main__': cli()
