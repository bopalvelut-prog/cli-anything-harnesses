import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('exchange running')
@cli.command()
def start(): click.echo('exchange started')
if __name__ == '__main__': cli()
