import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brother running')
@cli.command()
def start(): click.echo('brother started')
if __name__ == '__main__': cli()
