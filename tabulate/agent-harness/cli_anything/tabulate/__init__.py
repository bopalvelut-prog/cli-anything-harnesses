import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tabulate running')
@cli.command()
def start(): click.echo('tabulate started')
if __name__ == '__main__': cli()
