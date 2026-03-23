import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rgb running')
@cli.command()
def start(): click.echo('rgb started')
if __name__ == '__main__': cli()
