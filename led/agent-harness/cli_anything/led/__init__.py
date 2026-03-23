import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('led running')
@cli.command()
def start(): click.echo('led started')
if __name__ == '__main__': cli()
