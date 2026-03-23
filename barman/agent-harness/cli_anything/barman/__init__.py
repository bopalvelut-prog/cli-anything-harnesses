import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('barman running')
@cli.command()
def start(): click.echo('barman started')
if __name__ == '__main__': cli()
