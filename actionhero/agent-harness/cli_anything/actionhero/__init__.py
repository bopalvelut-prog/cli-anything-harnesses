import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('actionhero running')
@cli.command()
def start(): click.echo('actionhero started')
if __name__ == '__main__': cli()
