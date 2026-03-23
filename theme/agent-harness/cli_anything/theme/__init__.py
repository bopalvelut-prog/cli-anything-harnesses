import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('theme running')
@cli.command()
def start(): click.echo('theme started')
if __name__ == '__main__': cli()
