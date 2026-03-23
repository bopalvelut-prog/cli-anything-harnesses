import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lb running')
@cli.command()
def start(): click.echo('lb started')
if __name__ == '__main__': cli()
