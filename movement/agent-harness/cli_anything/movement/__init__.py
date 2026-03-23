import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('movement running')
@cli.command()
def start(): click.echo('movement started')
if __name__ == '__main__': cli()
