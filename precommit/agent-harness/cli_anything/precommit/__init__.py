import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('precommit running')
@cli.command()
def start(): click.echo('precommit started')
if __name__ == '__main__': cli()
