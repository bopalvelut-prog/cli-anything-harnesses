import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('relax running')
@cli.command()
def start(): click.echo('relax started')
if __name__ == '__main__': cli()
