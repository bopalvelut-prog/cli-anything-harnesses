import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('male running')
@cli.command()
def start(): click.echo('male started')
if __name__ == '__main__': cli()
