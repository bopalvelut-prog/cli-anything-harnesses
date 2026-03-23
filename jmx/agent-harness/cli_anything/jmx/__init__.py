import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jmx running')
@cli.command()
def start(): click.echo('jmx started')
if __name__ == '__main__': cli()
